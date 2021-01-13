class Firma:

    __TVA = 0

    def __init__(self):
        self.__profit = 0

    def set_profit(self, value):
        if value >= 0:
            self.__profit += value

    def get_proft(self):
        return self.__profit

    @classmethod
    def set_new_TVA(cls, tva):
        cls.__TVA = tva

    @classmethod
    def get_tva(cls):
        return cls.__TVA


lidl = Firma()
google = Firma()

print(lidl.get_proft())

