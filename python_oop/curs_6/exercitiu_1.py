"""
    Trivia:
    -
"""
from abc import ABC, abstractstaticmethod
from functools import reduce


class Question:
    """
    @:param question, answers, points
    """

    def __init__(self, question, answers, points):
        self.question = question
        self.answers = answers
        self.points = points

    def __str__(self):
        return f"{self.question} worth {self.answers}"


class Parser(ABC):

    @staticmethod
    def read_question(file):
        pass


class FileParser(Parser):
    def __init__(self):
        self.text = ''

    def read_question(self, file):
        with open(file, 'r') as f:
            self.text = f.readlines()
        return self.text

    def create_question(self):
        for index, line in self.text:
            if index == 0 or index // 6 == 0:
                pass


class UnknownArguments:
    def __init__(self, *args):
        self.name = args
        self.last_name = args


elvis = UnknownArguments('ELvis', 'Munteanu')

print(f'{elvis.name} {elvis.last_name}')



def print_dec(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_dec
def add_numbers2(*args, **kwargs):
    val = [x for x in kwargs.values() if x is not None]
    return reduce(lambda a, b: a + b, list(args).extend(list(val)))


add_numbers2(1, 3)
