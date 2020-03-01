from __future__ import annotations
from abc import ABC, abstractmethod

from product import ConcreteProduct1, ConcreteProduct2


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: worker with {product.operation()}"


class Creator1(Creator):

    def factory_method(self) -> ConcreteProduct1:
        return ConcreteProduct1()


class Creator2(Creator):

    def factory_method(self) -> ConcreteProduct2:
        return ConcreteProduct2()


