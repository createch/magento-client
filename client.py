from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import

# import logging
# logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)  # MUST BE THIS?
# logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
# logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)
# logging.getLogger('suds.resolver').setLevel(logging.DEBUG)
# logging.getLogger('suds.xsd.query').setLevel(logging.DEBUG)
# logging.getLogger('suds.xsd.basic').setLevel(logging.DEBUG)
# logging.getLogger('suds.binding.marshaller').setLevel(logging.DEBUG)

def get_magento_products(username, password):

    url = 'http://magento.localhost/api/v2_soap/?wsdl'
    imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
    # imp.filter.add('http://some/namespace/A')
    doctor = ImportDoctor(imp)
    client = Client(url)

    session = client.service.login('username', 'abc123')
    products = client.service.catalogProductList(session)
    skus = [product['sku'] for product in products]
    inventory = client.service.catalogInventoryStockItemList(session, skus)
    ordoro_products = []

    transformed = dict([(int(inv.product_id), inv) for inv in inventory])

    for product in products:
        prod = {
            "sku": product.sku,
            "cart_specific_id": product.product_id,
            "quantity": transformed[int(product.product_id)].qty
        }
        ordoro_products.append(prod)
    
# client.service.catalogInventoryStockItemList(session, skus)

# for product in products:
# print client.service.catalogProductList(session, [{'complex_filter': [{
#     'key': 'type',
#     'value': [{
#         'key': 'in',
#         'value': 'simple,configurable'}]}]
# }])

# print client.service.catalogProductLinkList(session, 'related', '1')
