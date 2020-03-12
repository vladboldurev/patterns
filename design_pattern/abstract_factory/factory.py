from __future__ import annotations
from abc import ABC, abstractmethod

from product import ConcreteProductA1, ConcreteProductA2,\
                     ConcreteProductB1, ConcreteProductB2,\
                     AbstractProductA, AbstractProductB


class AbstractFactory(ABC):

    @abstractmethod
    def create_product_a(self) -> AbstracProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):

    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):

    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()
