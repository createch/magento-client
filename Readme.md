
magento-client
==

A simple client for the Magento SOAP v2 API.

Requirements
--

suds - `pip install suds`


Usage
--

Get a list of all the products from our Magento instance.

```
m = apilib.MagentoClient('username', 'abc123', 'http://magento.localhost/api/v2_soap/?wsdl')
m_products = m.get_products()
```

Update the quantity levels for the first three products.

```
m_products[0]['quantity'] = 3
m_products[1]['quantity'] = 4
m_products[2]['quantity'] = 5
m.update_products(m_products[0:3])
```

Tests
--

See the `tests.py` file. Creates an instance of the MagentoClient and tests for the following:

- The session key should be a string
- The skus for products function should return strings in a specific format
- The inventory_to_dict function correctly converts the inventory list into a dict
- The product_format function correctly creates a dict using the product and inventory info
- The get_products should get a list of dicts with SKUs that are suds strings
