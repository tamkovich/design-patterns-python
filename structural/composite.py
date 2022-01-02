from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class ProductComponent(ABC):
    @property
    def parent(self) -> ProductComponent:
        return self._parent

    @parent.setter
    def parent(self, parent: ProductComponent):
        """
        При необходимости базовый Компонент может объявить интерфейс для
        установки и получения родителя компонента в древовидной структуре. Он
        также может предоставить некоторую реализацию по умолчанию для этих
        методов.
        """

        self._parent = parent

    """
    В некоторых случаях целесообразно определить операции управления потомками
    прямо в базовом классе Компонент. Таким образом, вам не нужно будет
    предоставлять конкретные классы компонентов клиентскому коду, даже во время
    сборки дерева объектов. Недостаток такого подхода в том, что эти методы
    будут пустыми для компонентов уровня листа.
    """

    def add(self, component: ProductComponent) -> None:
        pass

    def remove(self, component: ProductComponent) -> None:
        pass

    def is_composite(self) -> bool:
        """
        Вы можете предоставить метод, который позволит клиентскому коду понять,
        может ли компонент иметь вложенные объекты.
        """

        return False

    @abstractmethod
    def operation(self) -> str:
        """
        Базовый Компонент может сам реализовать некоторое поведение по умолчанию
        или поручить это конкретным классам, объявив метод, содержащий поведение
        абстрактным.
        """

        pass


class IPhone(ProductComponent):
    def operation(self) -> str:
        return "Iphone"


class MacBook(ProductComponent):
    def operation(self) -> str:
        return "MacBook"


class AirPods(ProductComponent):
    def operation(self) -> str:
        return "AirPods"


class AirTag(ProductComponent):
    def operation(self) -> str:
        return "AirTag"


class BoxComposite(ProductComponent):
    """
    Класс Контейнер содержит сложные компоненты, которые могут иметь вложенные
    компоненты. Обычно объекты Контейнеры делегируют фактическую работу своим
    детям, а затем «суммируют» результат.
    """

    def __init__(self) -> None:
        self._children: List[ProductComponent] = []

    def add(self, component: ProductComponent) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: ProductComponent) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(component: ProductComponent) -> None:
    """
    Клиентский код работает со всеми компонентами через базовый интерфейс.
    """

    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: ProductComponent, component2: ProductComponent) -> None:
    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    simple = IPhone()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    tree = BoxComposite()

    branch1 = BoxComposite()
    branch1.add(MacBook())
    branch1.add(AirPods())

    branch2 = BoxComposite()
    branch2.add(AirTag())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)
