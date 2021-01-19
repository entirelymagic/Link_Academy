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

    def run(self):
        return self


lidl = Firma()
google = Firma()

print(google.run().run().run())
# run method returns self( the object itself) so it can be used repeatedly as the object itself has the method run()
