import unittest
import suds
from apilib import MagentoClient

class TestMagentoClient(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        self.m = MagentoClient('username', 'abc123')
        print type(self.m.session)
        self.assertIsInstance(self.m.session, suds.sax.text.Text)

    def test_skus_for_products_catalog():
        
        m.skus_for_products_catalog()                


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

