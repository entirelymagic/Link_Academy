class Firma:

    __TVA = 0

    def __init__(self):
        self.__profit = 0

    def set_profit(self, value):
        if value >= 0:
            self.__profit += value

    def get_proft(self):
        return self.__profit


lidl = Firma()
google = Firma()

print(lidl.get_proft())

