from laptop import Laptop


class Manager:
    @staticmethod
    def count_total_cost(laptops):
        if isinstance(laptops, (list, tuple)):
            total_cost = 0
            for laptop in laptops:
                if isinstance(laptop, Laptop):
                    total_cost += laptop.price

            return total_cost

    @staticmethod
    def max_price(laptops):
        if isinstance(laptops, (list, tuple)):
            max_price = laptops[0].price
            for laptop in laptops:
                if isinstance(laptop, Laptop) and max_price < laptop.price:
                    max_price = laptop.price

            return max_price

    @staticmethod
    def min_price(laptops):
        if isinstance(laptops, (list, tuple)):
            min_price = Manager.max_price(laptops)
            for laptop in laptops:
                if isinstance(laptop, Laptop) and min_price > laptop.price:
                    min_price = laptop.price

            return min_price
