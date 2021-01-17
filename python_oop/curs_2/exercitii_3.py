"""
Partea 1:


    Creati 3 obiecte folosind 2 clase. Primul obiect sa fie o clasa numita Bucatarie(va fi doar una generala)si sa c
ontina ca atribute de tip clasa urmatoarele:
    - o lista in care sa fie listate ustensilele folosite(linguri, furculite),
    - un atribut care sa contina numarul maxim de oameni ce pot lucransimultan.
    - un alt atribut care sa contina numarul de cuptoare.

    Celelalte 2 obiecte sa fie instantiate din clasa numita Bucatari. Aceasta sa contina ca atribute:
    Numele, prenumele, experienta( numar de ani).

    Dupa crearea celor 3 obiecte introduceti 3 ustensile pentru clasa Bucatarie si 2 cuptoare, dar de asemenea
setati numarul maxim de bucatari ca fiind 2.
    Printati toate atributele fiecarui obiect creat.

Partea 2:


    Adaugam si metode(actiuni ce se pot face asupra obiectelor):
    Pentru Bucatarie cream urmatoarele metode de tip clasa(@classmethod):
    Schimbam atributul ce contine numarul maxim de oameni din public in unul privat si folosim getter si setteri
pentru a vizualiza si schimba numarul acestora. Shimbati numarul de bucatari de la 2 la 3 folosing noua metoda
creata

    Printati toate atributele clasei Bucatarie.

"""


class Bucatarie:
    """Clasa de tip bucatarie ce contine atribute de tip clasa"""
    ustensile = []
    __numarul_maxim_de_bucatari = 0
    numarul_de_cuptoare = 0

    @classmethod
    def set_numarul_maxim_de_bucatari(cls, noul_numar):
        """Un setter pentru atributul privat __numarul_maxim_de_bucatari ce ia ca parametru noul_numar
        si il seteaza ca fiind noul numar maxim de bucatari acceptati in bucatarie."""
        cls.__numarul_maxim_de_bucatari = noul_numar

    @classmethod
    def get_numarul_maxim_de_bucatari(cls):
        """Preia numarul maxim de bucatari din atributul privat __numarul_maxim_de_bucatari si il returteanza pentruf
        a putea fi folosit"""
        return cls.__numarul_maxim_de_bucatari


class Bucatari:
    """O clasa de tip Bucatari ce contine 3 atribute ce sunt construite pentru fiecare instanta in parte obiectelor
    de tip Bucatari ce vor fi create."""

    def __init__(self, nume, prenume, ani_experienta):
        self.nume = nume
        self.prenume = prenume
        self.ani_experienta = ani_experienta


bucatarie = Bucatarie()  # instantiem clasa Bucatari si o atribuim variabile bucatarie

# adaugam un nou ustensil in atributul de tip lista(ustensile) la obiectul de tip clasa bucatarie
bucatarie.ustensile.append("Furculite")
bucatarie.ustensile.append("Linguri")
bucatarie.ustensile.append("Polonice")

# setam numarul de cuptoare ca fiind 2
bucatarie.numarul_de_cuptoare = 2
# bucatarie.numarul_maxim_de_bucatari = 2

# instantiem 2 obiecte noi de tip Bucatari si le atribuim parametrii necesari crearii acestora
elvisMunteanu = Bucatari("Elvis", "Munteanu", 1)
dragosPopescu = Bucatari("Dragos", "Popescu", 3)

# Primtam atributele fiecarui obiect creat.
print(elvisMunteanu.nume)
print(elvisMunteanu.prenume)
print(elvisMunteanu.ani_experienta)

# Dupa schimbarea atributului numarul_maxim_de_bucatari din public in privat(prin atribuirea celor 2 linii jos __)
# acesta nu mai poate fi accesat fara un getter sau setter.

# setarea noului numar maxim de bucatari folosind un setter(metoda de setare si schimbare a atributelor)
print(bucatarie.set_numarul_maxim_de_bucatari(3))

print(bucatarie.ustensile)
print(bucatarie.numarul_de_cuptoare)
# setarea noului numar maxim de bucatari folosind un getter(metoda de returnare a atributelor)
print(bucatarie.get_numarul_maxim_de_bucatari())

# De mentionat ca setterii si geterii pot fi folositi pentru atribute private sau publice
# Fara crearea acestora pentru atribute private(cu double dunderscore __ ) nu se poate interactiona cu acestea
