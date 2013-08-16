from suds.client import Client


def enable_logging():
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)
    logging.getLogger('suds.transport').setLevel(logging.DEBUG)
    # logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
    # logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)
    # logging.getLogger('suds.resolver').setLevel(logging.DEBUG)
    # logging.getLogger('suds.xsd.query').setLevel(logging.DEBUG)
    # logging.getLogger('suds.xsd.basic').setLevel(logging.DEBUG)
    # logging.getLogger('suds.binding.marshaller').setLevel(logging.DEBUG)


def products_to_skus(products):
    return dict([(int(prod.product_id), prod) for prod in products])


def get_magento_products(api, session):
    """ Gets products from Magento's API """
    products = api.catalogProductList(session)
    skus = [product['sku'] for product in products]
    inventory = api.catalogInventoryStockItemList(session, skus)
    transformed = products_to_skus(inventory)
    ordoro_products = []
    for product in products:
        ordoro_products.append({
            "sku": product.sku,
            "cart_specific_id": product.product_id,
            "quantity": transformed[int(product.product_id)].qty
        })
    return ordoro_products


def set_magento_products_inventory(api, session, products):
    """ Updates the product quantity for the specified products in Magento """
    for product in products:
        api.catalogInventoryStockItemUpdate(session, product['cart_specific_id'], {'qty': product['quantity']})


def get_api_products(ordoro_url, ordoro_key):
    """ Simulates querying products from Ordoro's API """
    return [{'sku': 'n2610', 'quantity': 996.0000, 'cart_specific_id': 16},
            {'sku': 'bb8100', 'quantity': 797.0000, 'cart_specific_id': 17}]


def main():
    username = 'username'
    password = 'abc123'
    magento_url = 'http://magento.localhost/api/v2_soap/?wsdl'
    client = Client(magento_url)
    api = client.service
    session = client.service.login(username, password)
    products = get_magento_products(api, session)
    print "Before:", products[0:3]
    products[0]['quantity'] = 3
    products[1]['quantity'] = 4
    products[2]['quantity'] = 5
    set_magento_products_inventory(api, session, products[0:3])
    products = get_magento_products(api, session)
    print "After:", products[0:3]
    print "Get Ordoro API Products: ", get_api_products('http://fake.com', 'trollolol')


if __name__ == "__main__":
    main()
