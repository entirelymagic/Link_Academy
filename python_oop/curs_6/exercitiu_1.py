"""
    Trivia:
    -
"""
from abc import ABC, abstractstaticmethod


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



