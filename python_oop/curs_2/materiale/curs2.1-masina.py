###########
# Creati o clasa pentru categoria Masina care sa contina: 
# Marca, Consum, Nr de km parcursi, Pret combustibil
# Alimentare benzina si combustibil disponibil
# Parcurgere kilometrii
# Bani cheltuiti cu masina (consumul)
############

class Masina:
    def __init__(self, marca, consum, cap_rezervor=50):
        self.__marca = marca
        self.consum = consum
        self.km_parcursi = 0
        self.cantitate_benzina = 0
        self.cap_rezervor = cap_rezervor

    def get_marca(self):
        return self.__marca

    def set_marca(self, new_marca):
        return self.__marca

    def verifica_benzina_disponibila(self, noi_km_parcursi):
        benzina_consumata = (self.consum * noi_km_parcursi) / 100
        if self.cantitate_benzina >= benzina_consumata:
            return True
        else:
            return False

    def parcurge_km(self, noi_km_parcursi):
        if self.verifica_benzina_disponibila(noi_km_parcursi):
            benzina_consumata = (self.consum * noi_km_parcursi) / 100
            self.km_parcursi = (noi_km_parcursi + self.km_parcursi)
            self.cantitate_benzina = self.cantitate_benzina - benzina_consumata
            print("Putem Incepe")
        else:
            print("Nu putem incepe")

    def alimenatare(self, benzina):
        if benzina <= (self.cap_rezervor - self.cantitate_benzina):
            self.cantitate_benzina = self.cantitate_benzina + benzina
        else:
            self.cantitate_benzina = self.cap_rezervor
        return self.cantitate_benzina


mercedes = Masina("Eclass", 7)
mercedes.alimenatare(20)
print(mercedes.cantitate_benzina)
este_disponibil = mercedes.verifica_benzina_disponibila(50)
mercedes.parcurge_km(50)
mercedes.parcurge_km(100)
print(este_disponibil)
print(mercedes.cantitate_benzina)
mercedes.alimenatare(1000)
print(mercedes.cantitate_benzina)

mercedes.cantitate_benzina = 200
