import apilib


def main():
    m = apilib.MagentoClient('username', 'abc123')
    o = apilib.OrdoroClient('ordorokey123abclololol')
    print m
    print o

if __name__ == '__main__':
    main()
