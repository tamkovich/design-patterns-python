from __future__ import annotations
from abc import ABC, abstractmethod


class MultiPlatformFrameworkAbstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"MultiPlatformFrameworkAbstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class DjangoAbstraction(MultiPlatformFrameworkAbstraction):
    def operation(self) -> str:
        return (f"DjangoAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class IOSImplementation(Implementation):
    def operation_implementation(self) -> str:
        return "IOSImplementation: Here's the result on the platform IOS."


class LinuxImplementation(Implementation):
    def operation_implementation(self) -> str:
        return "LinuxImplementation: Here's the result on the platform Linux."


def client_code(abstraction: MultiPlatformFrameworkAbstraction) -> None:
    print(abstraction.operation(), end="")


if __name__ == "__main__":
    implementation = IOSImplementation()
    abstraction = MultiPlatformFrameworkAbstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = LinuxImplementation()
    abstraction = DjangoAbstraction(implementation)
    client_code(abstraction)
