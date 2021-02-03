"""
mostenirea

polimorfismul

incalpsularea

Singleton:

Decoratori:


"""
import abc
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

    @property
    @abstractmethod
    def hair(self):
        pass

