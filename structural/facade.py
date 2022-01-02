from __future__ import annotations


class Facade:
    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.make_ready())
        results.append(self._subsystem2.make_ready())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.run())
        results.append(self._subsystem2.run())
        return "\n".join(results)


class Subsystem1:
    def make_ready(self) -> str:
        return "Subsystem1: Ready!"

    def run(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2:
    def make_ready(self) -> str:
        return "Subsystem2: Get ready!"

    def run(self) -> str:
        return "Subsystem2: Fire!"


def client_code(facade: Facade) -> None:
    print(facade.operation(), end="")


if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
