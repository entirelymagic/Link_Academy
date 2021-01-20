# Creati o clasa Depozit pentru a depozita mancarea. 
# Depozitul va contine tipuri de mancare si capacitatea maxima.

class Depozit:
    __CAPACITATE_MAXIMA_PERMISA = 1000
    def __init__(self):
        self.__capacitatce_curenta = 0

    def adauga(self, cantitate):
        
         capacitate_totala = self.__capacitatce_curenta + cantitate
         if capacitate_totala <= Depozit.__CAPACITATE_MAXIMA_PERMISA:
             self.__capacitatce_curenta = capacitate_totala
    
    @classmethod
    def set_capacitate_maxima(cls, capacitate_noua):
        Depozit.__CAPACITATE_MAXIMA_PERMISA = capacitate_noua

    @classmethod
    def get_capacitate_maxima(cls):
        return Depozit.__CAPACITATE_MAXIMA_PERMISA

    def set_capacitate_curenta(self, capacitate):
        self.__capacitatce_curenta = self.__capacitatce_curenta + capacitate

    def get_capacitate_curenta(self):
        return self.__capacitatce_curenta
    

kaufland = Depozit()
lidl = Depozit()

kaufland.set_capacitate_curenta(300)
kaufland.set_capacitate_maxima(3500)
print(kaufland.get_capacitate_maxima())
print(lidl.get_capacitate_maxima())
print(kaufland.get_capacitate_curenta())
print(lidl.get_capacitate_curenta())