import apilib


def main():
    m = apilib.MagentoClient('username', 'abc123')
    m_products = m.get_products()
    m_products[0]['quantity'] = 3
    m_products[1]['quantity'] = 4
    m_products[2]['quantity'] = 5
    m.update_products(m_products[0:3])
    o = apilib.OrdoroClient('ordorokey123abclololol')
    o_products = o.get_products()

if __name__ == '__main__':
    main()
