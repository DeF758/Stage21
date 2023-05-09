'''
task03
v.1.0
Gerasimchik D.Y.
QA2022
09.05.2023
'''
from laptop_creator import LaptopCreator
from manager import Manager


def main():
    ls = LaptopCreator.create()
    for laptop in ls:
        print(laptop)

    total_cost = Manager.count_total_cost(ls)

    max_price = Manager.max_price(ls)

    min_price = Manager.min_price(ls)
    print(f"Total cost: {total_cost}$"
          f"\nMaximum cost: {max_price}$"
          f"\nMinimum cost: {min_price}$")


if __name__ == '__main__':
    main()
