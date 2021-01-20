class Animal:
    breathe = True


class Mamifer(Animal):
    naste_pui_vii = True


class Caine(Mamifer):
    def __init__(self, nume='Tomberonez'):
        self.nume = nume

    def speak(self):
        print('Ham ham ham!')


grivei = Caine('Caine Android')

grivei.speak()
print(grivei.naste_pui_vii)
print(grivei.breathe)
