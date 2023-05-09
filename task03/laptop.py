class Laptop:
    def __init__(self, brand='no brand', model='no model', price='185'):
        self.__brand = brand
        self.__model = model
        self.__prise = price

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if isinstance(model, str):
            self.__model = model

    @property
    def price(self):
        return self.__prise

    @price.setter
    def price(self, price):
        if isinstance(price, int) and price > 50:
            self.__prise = price

    def __str__(self):
        return f"{self.brand}, {self.model} - {self.price}$"
