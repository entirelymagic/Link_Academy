from datetime import datetime
from db_gestiune_magazin import save_to_db, return_data

SET_CATEGORII = {'barbati', 'femei', 'copii', 'accesorii', 'casa', 'deluxe'}


class Product:
    def __init__(self, name, price, *categorie):
        self.name = name
        self.price = price
        self.categorii = set()
        for i in categorie:  # verificam daca sunt mai multe categorii
            if i in SET_CATEGORII:  # verificam daca categoria face parte din categoriile existente
                self.categorii.add(i)  # sunt adaugate categoriile produsului


class Magazin:
    def __init__(self, name):
        self.name = name
        self.vanzari = list()  # TODO: De adaugat datele de vanzare

    def vanzare(self, cumparator, product):
        now = datetime.now()
        vanzare = {
            'cumparator': cumparator,
            'produs': {
                'name': product.name,
                'price': product.price,
                'categorii': product.categorii,
            },
            'date_of_sell': str(now),
            'retur': False,
            'retur_date': False
        }

        save_to_db(str(vanzare))
        self.vanzari.append(vanzare)

    def anulare_comanda(self, cumparator, product):
        for i in self.vanzari:
            if i['cumparator'] == cumparator and i['produs']['name'] == product.name and i['retur'] == False:
                i['retur'] = True
                now = datetime.now()
                i['retur_date'] = str(now)

    def valoare_vanzari(self):
        """Returneaza totalul al vanzarilor ce au  si numarul fara cele returnate"""
        total_vanzari = 0
        nr_comenzi = 0
        for i in emag.vanzari:
            if not i['retur']:
                nr_comenzi += 1
                total_vanzari += i['produs']['price']
        return total_vanzari, nr_comenzi

    def total_valaore_retur(self):
        """Returneaza totalul vanzarilor ce au fost returnate, si numarul """
        total_vanzari = 0
        nr_comenzi = 0
        for i in emag.vanzari:
            if i['retur']:
                nr_comenzi += 1
                total_vanzari += i['produs']['price']
        return total_vanzari, nr_comenzi


ceas_gucci_model_001 = Product('Ceas', 100, 'barbati', 'femei')
emag = Magazin('Emag')
emag.vanzare('Elvis', ceas_gucci_model_001)
emag.anulare_comanda('Elvis', ceas_gucci_model_001)

papuci_piele_crocodil = Product('Piele de smecher', 2900, 'barbati', 'deluxe')
emag.vanzare('Dragos', papuci_piele_crocodil)

print(emag.vanzari)

print(emag.valoare_vanzari())
print(emag.total_valaore_retur())
