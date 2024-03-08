from main.Product import Product


class Category:
    """Описание категории товаров"""

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self.__products)}'

    def get_products(self):
        result = ''
        for product in self.__products:
            result += f'{product.name}, {product.price}, остаток {product.remain}'
        return result

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, new_product):
        get_object = Product(name=new_product['name'], description=new_product['description'],
                             price=new_product['price'], quantity=new_product['quantity'])
        if isinstance(new_product, Product):
            self.__products.append(get_object)
        else:
            raise TypeError
