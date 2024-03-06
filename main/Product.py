from abc import ABC

class AbstrcProduct():

    def __init__(self, name, description, price, remain):
        self.name = name
        self.description = description
        self._price = price
        self.remain = remain


    @absreactmethod
    def name(self):
        return f'Ваш продукт - {self.name}'


class Product(AbstrcProduct):
    """Описание конкретного товара"""

    def __init__(self, name, description, price, remain):
        super().__init__(name, description, price, remain)

    def name(self):
        return f'Ваш продукт - {self.name}'

    def __str__(self):
         return f'{self.name}, {self.price}. Остаток: {self.remain} шт.'

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.price * self.remain + other.price * other.remain
        else:
            raise TypeError

    @classmethod
    def new_product(cls, name, description, price, remain):
        cls.new_product = name, description, price, remain
        return cls(dict(name=name, description=description, price=price, remain=remain))

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if int(new_price) <= 0:
            print(f'Цена введена некорректно')
        else:
            self._price = new_price


class MixinRepr:

    def __init__(self, object):
        self.object = object

    def __repr__(self):
        return f'{self.__class__.__name__}, {self.object}'


class Smartphones(Product):

    def __init__(self, efficiency, model, memory, color, name, description, price, remain):
        super().__init__(name, description, price, remain)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def name(self):
        return f'Ваш продукт - {self.name}'

class LawnGrass(Product):

    def __init__(self, country_of_origin, germination_time, color, name, description, price, remain):
        super().__init__(name, description, price, remain)
        self.country_of_origin = country_of_origin
        self.germination_time = germination_time
        self.color = color

    def name(self):
        return f'Ваш продукт - {self.name}'
