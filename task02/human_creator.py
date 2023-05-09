from random import choice, randint
from human import Human
from string import ascii_uppercase


class HumanCreator:
    @staticmethod
    def create(size=10):
        humans = []
        NAMES = ("Alex", "Peter", "Garry", "Alice", "Vladimie",
                 "Olga", "Anna", "Kate", "Victor", "Max")

        MAX_AGE = 120
        MIN_AGE = 1

        for _ in range(size):
            human = Human()
            human.name = choice(NAMES)
            human.name += " " + choice(ascii_uppercase) + "."

            human.age = randint(MIN_AGE, MAX_AGE)

            human.is_alive = choice((True, False))

            humans.append(human)
        return humans
