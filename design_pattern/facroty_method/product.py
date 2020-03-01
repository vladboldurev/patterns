from __future__ import annotations
from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def operation(self):
        pass


class ConcreteProduct1(Product):

    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):

    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"