class Firma:

    def __init__(self):
        self.__profit = 0
        # Profit - specific pt fiecare firma in parte

    def set_profit(self, value):
        if value > 0:
            self.__profit = value
        else:
            self.__profit = 0

    def get_profit(self):
        return self.__profit

    # TVA - general pt toate firmele 
    __TVA = 19

    @classmethod
    def set_TVA(cls, TVA_noua):
        Firma.__TVA = TVA_noua

    @classmethod
    def get_TVA(cls):
        return Firma.__TVA


kaufland = Firma()
lidl = Firma()

kaufland.set_profit(12)
kaufland.set_TVA(19)

print("TVA kaufland: " + str(kaufland.get_TVA()))
print("Profit kaufland: " + str(kaufland.get_profit()))

print("TVA lidl: " + str(lidl.get_TVA()))
print("Profit lidl: " + str(lidl.get_profit()))
