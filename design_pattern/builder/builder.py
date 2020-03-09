from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any

from product import Product1


class Builder(ABC):

    @abstractproperty
    def product(self) -> None:
        pass

    def product_part_a(self):
        pass

    def product_part_b(self):
        pass

    def product_part_c(self):
        pass


class ConcreteBuilder1(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self) -> Product1():
        product = self._product
        self.reset()
        return product

    def product_part_a(self):
        self._product.add("Part_a")

    def product_part_b(self):
        self._product.add("Part_b")

    def product_part_c(self):
        self._product.add("Part_c")


