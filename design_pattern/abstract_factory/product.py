from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractProductA(ABC):

    @abstractmethod
    def useful_function(self) -> str:
        pass


class AbstractProductB(ABC):

    @abstractmethod
    def useful_function(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):

    def useful_function(self) -> str:
        print('useful function concrete product A1')


class ConcreteProductB1(AbstractProductB):

    def useful_function(self) -> str:
        print('useful function concrete product B1')


class ConcreteProductA2(AbstractProductA):

    def useful_function(self) -> str:
        print('useful function concrete product A2')


class ConcreteProductB2(AbstractProductB):

    def useful_function(self) -> str:
        print('useful function concrete product B2')
