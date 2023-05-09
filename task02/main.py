'''
task02
v.1.0
Gerasimchik D.Y.
QA2022
07.05.2023
'''
from human_creator import HumanCreator
from manager import Manager


def main():
    ls = HumanCreator.create()

    for human in ls:
        print(human)

    adult = Manager.count_adult(ls)
    underage = Manager.count_underage(ls)

    print(f"Adult - {adult}")
    print(f"Underage - {underage}")

    alive = Manager.count_alive(ls)
    dead = Manager.count_dead(ls)

    print(f"Alive - {alive}")
    print(f"Dead - {dead}")


if __name__ == '__main__':
    main()
