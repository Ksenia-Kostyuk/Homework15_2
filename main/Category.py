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
        """Добавляет объект в список"""
        get_object = Product(name=new_product['name'], description=new_product['description'],
                             price=new_product['price'], quantity=new_product['quantity'])
        if new_product['quantity'] == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        elif isinstance(new_product, Product):
            self.__products.append(get_object)
        elif not isinstance(new_product, Product):
            raise TypeError

    def sum_price(self):
        """Подсчитывает средний ценник всех товаров"""
        result = 0
        try:
            for i in self.__products:
                result += i['price'] / i['quantity']
            return result
        except ZeroDivisionError:
            print(0)


#if __name__ == '__main__':
    #op = Category('Фрукты', 'Спелые', [{'name':'Яблоко', 'description':'Сладкое', 'price': 10, 'quantity': 10}, {'name':'Апельсин', 'description':'Спелый', 'price': 15, 'quantity': 6}])
    #print(op.sum_price())