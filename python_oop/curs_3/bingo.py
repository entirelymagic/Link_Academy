from random import randint


class Player:
    def __init__(self, name):
        self.name = name

    def player_name(self):
        return f'Player name is {self.name}'


class Lottery(Player):
    """A class that have a name and """
    __extracted_numbers = []
    __guessed_numbers = []
    _nr_of_winners = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }

    def __init__(self, name, numbers):
        super().__init__(name)
        self.numbers = numbers

    def __str__(self):
        return (f'''Extracted numbers are {self.__extracted_numbers}.
        Player numbers are {self.numbers}.
        Player {self.name} guest {len(self.__guessed_numbers)} : {self.__guessed_numbers}''')

    def __generate_new_numbers(self):
        self.__extracted_numbers.clear()
        self.__guessed_numbers.clear()
        while len(self.__extracted_numbers) <= 6:
            new_number = randint(1, 50)
            if new_number not in self.__extracted_numbers:
                self.__extracted_numbers.append(new_number)

    def check_winner(self):
        self.__generate_new_numbers()
        self.__guessed_numbers = []
        for num in self.numbers:
            if num in self.__extracted_numbers:
                self.__guessed_numbers.append(num)

        self._nr_of_winners[len(self.__guessed_numbers)] += 1
        if len(self.__guessed_numbers) == 6:
            print('Bingo!')
            global bingo
            bingo = True

        print(self.__str__())


alexandra = Lottery(name='Alexandra', numbers=[23, 27, 5, 9, 45, 42])
elvis = Lottery(name='Elvis', numbers=[14, 35, 19, 31, 40, 42])
bingo = False

while not bingo:
    elvis.check_winner()
    alexandra.check_winner()
    print(Lottery._nr_of_winners)
