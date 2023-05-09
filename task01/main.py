'''
task01
v.1.0
Gerasimchik D.Y.
QA2022
09.05.2023
'''
from zebra import Zebra
from zebra_creator import ZebraCreator


def main():
    z1 = Zebra()

    print(z1)
    print(z1)
    print(z1)
    print(z1)
    print(z1)
    print(z1)
    print()

    ls = ZebraCreator.create()

    for zebra in ls:
        print(zebra)
    print()

    for zebra in ls:
        print(zebra)
    print()

    for zebra in ls:
        print(zebra)
        print(zebra)


if __name__ == '__main__':
    main()
