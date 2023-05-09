from random import choice, randint
from laptop import Laptop


class LaptopCreator:
    @staticmethod
    def create(size=15):
        laptops = []
        BRAND = ("ASUS", "Lenovo", "Apple", "HP", "Samsung")

        MODEL_ASUS = ("Vivobook 16X", "ROG Strix G15", "TUF Gaming F15",
                      "VivoBook 14", "VivoBook Pro 15", "ROG Strix SCAR 16 2023")
        MODEL_LENOVO = ("Legion 5", "Legion 7", "IdeaPad Gaming 3",
                        "Legion 5 Pro", "Legion 7 Pro", "IdeaPad 3")
        MODEL_APPLE = ('Macbook Air 13" M1 2020', 'Macbook Air 13" M2 2022',
                       'Macbook Pro 14" M2 Pro 2023', 'Macbook Pro 14" M1 Max 2021',
                       'Macbook Pro 16" M1 Max 2021')
        MODEL_HP = ("HP Omen 17", "EliteBook 830 G9", "ZBook Fury 17 G8",
                    "255 G8", "250 G8")
        MODEL_SAMSUNG = ("Galaxy Book2 ", "Galaxy Book NP750",
                         "Galaxy Book Flex2 Alpha 13")

        MIN_PRICE = 270
        MAX_PRICE = 14337

        for _ in range(size):
            laptop = Laptop()
            laptop.brand = choice(BRAND)

            if laptop.brand == "ASUS":
                laptop.model = choice(MODEL_ASUS)
            elif laptop.brand == "Lenovo":
                laptop.model = choice(MODEL_LENOVO)
            elif laptop.brand == "Apple":
                laptop.model = choice(MODEL_APPLE)
            elif laptop.brand == "HP":
                laptop.model = choice(MODEL_HP)
            elif laptop.brand == "Samsung":
                laptop.model = choice(MODEL_SAMSUNG)

            laptop.price = randint(MIN_PRICE, MAX_PRICE)

            laptops.append(laptop)

        return laptops
