from abc import ABC, abstractmethod


class AbstrcProduct(ABC):
    """Определяет общий интерфейс классов"""

    @abstractmethod
    def codes(self):
        """Вывод количества товаров на складе"""
        pass


class Product(AbstrcProduct):
    """Описание конкретного товара"""

    def __init__(self, name, description, price, remain):
        self.name = name
        self.description = description
        self._price = price
        self.remain = remain

    def codes(self):
        return f'На складе {self.remain} шт.'

    @property
    def __str__(self):
        """Вывод товара, цены и его количества"""
        return f'{self.name}, {self.price}. Остаток: {self.remain} шт.'

    def __add__(self, other):
        """Вычисляет цену на весь ассортимент"""
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
            print('Цена введена некорректно')
        else:
            self._price = new_price


class MixinRepr:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f'''Класс миксин -> {self.__class__.__name__}, наименование продукты -> {self.name} 
        Описание товара -> {self.description}, цена - {self.price}, в наличии: {self.remain}'''


class Smartphones(Product):

    def __init__(self, efficiency, model, memory, color, name, description, price, remain):
        super().__init__(name, description, price, remain)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def codes(self):
        return f'На складе {self.remain} шт.'


class LawnGrass(Product):

    def __init__(self, country_of_origin, germination_time, color, name, description, price, remain):
        super().__init__(name, description, price, remain)
        self.country_of_origin = country_of_origin
        self.germination_time = germination_time
        self.color = color

    def codes(self):
        return f'На складе {self.remain} шт.'
