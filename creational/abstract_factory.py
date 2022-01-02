from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> AbstractChair:
        pass

    @abstractmethod
    def create_table(self) -> AbstractTable:
        pass


class ModernFurnitureFactory(AbstractFurnitureFactory):
    def create_chair(self) -> AbstractChair:
        return ModernChair()

    def create_table(self) -> AbstractTable:
        return ModernTable()


class VictorianFurnitureFactory(AbstractFurnitureFactory):
    def create_chair(self) -> AbstractChair:
        return VictorianChair()

    def create_table(self) -> AbstractTable:
        return VictorianTable()


class AbstractChair(ABC):
    @abstractmethod
    def sit(self) -> str:
        pass


class ModernChair(AbstractChair):
    def sit(self) -> str:
        return "modern chair"


class VictorianChair(AbstractChair):
    def sit(self) -> str:
        return "victorian chair"


class AbstractTable(ABC):
    @abstractmethod
    def clean(self) -> None:
        pass

    @abstractmethod
    def eat(self, chair: AbstractChair) -> None:
        pass


class ModernTable(AbstractTable):
    def clean(self) -> str:
        return "Modern table was cleaned, bro"

    def eat(self, chair: AbstractChair) -> str:
        result = chair.sit()
        return f"Wasap, bro, sid down here ({result}), yo"


class VictorianTable(AbstractTable):
    def clean(self) -> str:
        return "Victorian table was cleaned, monsieur"

    def eat(self, chair: AbstractChair):
        result = chair.sit()
        return f"Please sit on a {result} monsieur"


def client_code(factory: AbstractFurnitureFactory) -> None:
    """
    Клиентский код работает с фабриками и продуктами только через абстрактные
    типы: Абстрактная Фабрика и Абстрактный Продукт. Это позволяет передавать
    любой подкласс фабрики или продукта клиентскому коду, не нарушая его.
    """
    table = factory.create_table()
    chair = factory.create_chair()

    print(f"{table.clean()}")
    print(f"{table.eat(chair)}", end="")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ModernFurnitureFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(VictorianFurnitureFactory())
