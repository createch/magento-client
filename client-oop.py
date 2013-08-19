from suds.client import Client


class APIClient(object):

    def __init__(self):
        self.products = []
        pass

    def get_products(self):
        return self.products

    def update_products(self):
        pass


class MagentoClient(APIClient):

    def __init__(self, username, password):
        super(MagentoClient, self).__init()
        magento_url = 'http://magento.localhost/api/v2_soap/?wsdl'
        self.username = username
        self.password = password
        self.client = Client(magento_url)
        self.api = self.client.service
        self.session = self.api.login(username, password)

    def skus_for_products_catalog(self, products_cat):
        """ Returns a list of skus """
        return [product['sku'] for product in products_cat]

    def inventory_dict(self, products_cat):
        """ Returns a dictionary of products with product_id as the key.
            Allows us to do the look up in O(1) time. """
        dict([(prod.product_id, prod) for prod in products_cat])

    def product_format(self, product, stock):
        return {
            'sku': product.sku,
            'cart_specific_id': product.product_id,
            'quantity': stock[product.product_id].qty
        }

    def get_products(self):
        """ Gets the products from the API and returns them as a list of
            ordoro formatted products. """
        products_cat = self.api.catalogProductList(self.session)
        skus = self.skus_for_products_catalog(products_cat)
        inventory = self.api.catalogInventoryStockItemList(self.session, skus)
        inventory_dict = self.inventory_dict(inventory)
        for product in products_cat:
            inventory_status = inventory_dict[product.product_id]
            self.products.append(
                self.product_format(product, inventory_status))
        return self.products

    def update_products(self, products):
        """ Updates the quantity of each product in the ordoro formatted list
            of products. """
        for product in products:
            id = product['cart_specific_id']
            changes = {'qty': product['quantity']}
            self.api.catalogInventoryStockItemUpdate(self.session, id, changes)


class OrdoroClient(APIClient):

    def __init__(self, apikey):
        super(OrdoroClient, self).__init()
        ordoro_url = 'http://ordoro.com/api/'
        self.apikey = apikey

    def get_products():
        return [{'sku': 'n2610', 'quantity': 996.0000, 'cart_specific_id': 16},
            {'sku': 'bb8100', 'quantity': 797.0000, 'cart_specific_id': 17}]
