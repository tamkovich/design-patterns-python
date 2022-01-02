from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class HouseBuilder(ABC):
    def __init__(self) -> None:
        self._product = HouseProduct()

    def reset(self) -> None:
        self._product = HouseProduct()

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def build_garage(self) -> None:
        pass

    @abstractmethod
    def build_swimming_pool(self) -> None:
        pass


class HouseWithGarageBuilder(HouseBuilder):
    @property
    def product(self) -> HouseProduct:
        product = self._product
        self.reset()
        return product

    def build_garage(self) -> None:
        self._product.add("Super fancy garage")

    def build_swimming_pool(self) -> None:
        self._product.add("Empty swimming pool")


class HouseWithSwimmingPool(HouseBuilder):
    @property
    def product(self) -> HouseProduct:
        product = self._product
        self.reset()
        return product

    def build_garage(self) -> None:
        self._product.add("Super fancy garage")

    def build_swimming_pool(self) -> None:
        self._product.add("Super fancy swimming pool!")


class HouseProduct:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """Optional class allows you to build house by defined plan"""

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> HouseBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: HouseBuilder) -> None:
        self._builder = builder

    def build_minimal_viable_house(self) -> None:
        self.builder.build_garage()

    def build_full_featured_house(self) -> None:
        self.builder.build_garage()
        self.builder.build_swimming_pool()


if __name__ == "__main__":
    director = Director()
    builder = HouseWithGarageBuilder()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_house()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_house()
    builder.product.list_parts()

    print("\n")

    print("Custom product: ")
    builder = HouseWithSwimmingPool()
    builder.build_garage()
    builder.build_swimming_pool()
    builder.product.list_parts()
