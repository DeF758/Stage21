class Zebra:
    def __init__(self, name='Zebra', stripe=True):
        self.__name = name
        self.__stripe = stripe

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    @property
    def stripe(self):
        if self.__stripe:
            self.__stripe = False
            return False
        else:
            self.__stripe = True
            return True

    def __str__(self):
        return f"{self.name} - " \
            + ("white line" if self.stripe else "black line")
