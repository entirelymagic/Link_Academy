class Student:
    def __init__(self, *curs):
        self.cursuri = []
        self.note = list()
        self.cursuri.append(curs)

    def __add__(self, curs_nou):
        self.cursuri.append(curs_nou)
        return Student(self.cursuri)

    def __str__(self):
        return f"{[curs for curs in self.cursuri]}"


class Curs:
    def __init__(self, nume):
        self.nume = nume

    def __eq__(self, alt_Curs):
        print(self.nume)
        print(alt_Curs)
        return self.nume == alt_Curs.nume


curs1 = Curs('Matematica')
curs3 = Curs('Matematica')
curs2 = Curs('Limba Romana')


x = Student('Mate')

y = Student("Romana")

x = x +curs1

print(x)