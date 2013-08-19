

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

