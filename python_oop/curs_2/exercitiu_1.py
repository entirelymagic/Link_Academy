class Masina:
    def __init__(self, marca, consum, cap_rezervor= 50):
        self.marca = marca
        self.consum = consum
        self.cap_rezervor = cap_rezervor
        self.cantitate_benzina = 0
        self.km_parcursi = 0
        self.bani_cheltuiti = 0
        self.valoare_benzina = 0

    def __alimentare(self, cantitate, pret):
        if cantitate <= self.cap_rezervor-self.cantitate_benzina:
            self.cantitate_benzina += cantitate
            self.valoare_benzina = cantitate*pret
            self.pret_benzina = pret

        else:
            self.cantitate_benzina = self.cap_rezervor
            return self.cantitate_benzina

    def parcurgere_distanta(self, distanta):

        benzina_consumata = (distanta*self.consum)/100

        if self.cantitate_benzina >= benzina_consumata:
            self.cantitate_benzina -= benzina_consumata
            self.km_parcursi += distanta
        else:
            self.cantitate_benzina = 0
            distanta_parcursa = self.cantitate_benzina/7*100
            self.km_parcursi += distanta_parcursa


mercedes = Masina("Eclass", 7)
mercedes.__alimentare(20,5)

print(mercedes.cantitate_benzina)

