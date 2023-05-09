from zebra import Zebra


class ZebraCreator:
    @staticmethod
    def create(size=8):
        zebras = []
        num = 1

        for _ in range(size):
            zebra = Zebra()
            zebra.name = "Zebra " + str(num)

            zebras.append(zebra)

            num += 1
        return zebras
