import unittest
import suds
from apilib import MagentoClient

class TestMagentoClient(unittest.TestCase):

    def setUp(self):
        self.m = MagentoClient('username', 'abc123')
        self.inventory_list = [{
            'product_id': '165',
            'sku': 'mycomputer',
            'qty': '79.0000',
            'is_in_stock': '1'
        }, {'product_id': '166',
            'sku': 'HTC Touch Diamond',
            'qty': '849.0000',
            'is_in_stock': '1'
            }]
        self.inventory_dict = {
            165: {
                'product_id': '165',
                'sku': 'mycomputer',
                'qty': '79.0000',
                'is_in_stock': '1'
            },
            166: {
                'product_id': '166',
                'sku': 'HTC Touch Diamond',
                'qty': '849.0000',
                'is_in_stock': '1'
            }}
        self.products_catalog = [{
            'product_id': 165,
            'sku': 'mycomputer',
            'name': 'My Computer',
            'set': 39,
            'type': 'bundle',
            'category_ids': [27],
            'website_ids': [1]
        }, {
            'product_id': 166,
            'sku': 'HTC Touch Diamond',
            'name': 'HTC Touch Diamond',
            'set': 38,
            'type': 'simple',
            'category_ids': [8],
            'website_ids': [1],
        }]
        self.formatted_product = {
            'sku': 'mycomputer',
            'cart_specific_id': 165,
            'quantity': '79.0000'
        }

    def test_init(self):
        self.assertIsInstance(self.m.session, suds.sax.text.Text)

    def test_skus_for_products_catalog(self):
        self.assertListEqual(['mycomputer', 'HTC Touch Diamond'],
                             self.m.skus_for_products_catalog(self.products_catalog))

    def test_inventory_to_dict(self):
        self.assertDictEqual(self.inventory_dict,
                             self.m.inventory_to_dict(self.inventory_list))

    def test_product_format(self):
        self.assertDictEqual(self.formatted_product,
                             self.m.product_format(self.products_catalog[0], self.inventory_dict[165]))

    def test_get_products(self):
        products = self.m.get_products()
        self.assertIsInstance(products, list)
        self.assertIsInstance(products[0], dict)
        self.assertIsInstance(products[0]['sku'], suds.sax.text.Text)


if __name__ == "__main__":
    unittest.main()

"""

MagentoClient()

__init__
    it should create an instance without a SOAP error
    it should populate the instance variable session with a string

skus_for_products_catalog
    it should return a list of strings that are the same as the skus in the input

inventory_dict
    it should return a dict with integers for the key
    it should have items with a sku, id, and quantity

product_format
    it should return a dictionary with a (str) sku, (int) cart_specific_id, and (int) quantity

get_products
    it should return a list of products

update_products
    it should have no errors (there has to be a better test?)


OrdoroClient()

__init__
    it should set self.apikey equal to apikey

get_products
    it should return a list of products

"""
