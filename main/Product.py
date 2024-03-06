class Product:
    """Описание конкретного товара"""

    def __init__(self, name, description, price, remain):
        self.name = name
        self.description = description
        self._price = price
        self.remain = remain

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


class Smartphones(Product):

    def __init__(self, name, description, price, remain, efficiency, model, memory, color):
        self.name = name
        self.description = description
        self._price = price
        self.remain = remain
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(self, name, description, price, remain, country_of_origin, germination_time, color):
        self.name = name
        self.description = description
        self._price = price
        self.remain = remain
        self.country_of_origin = country_of_origin
        self.germination_time = germination_time
        self.color = color