from __future__ import annotations
from abc import ABC, abstractmethod


class Logistic(ABC):
    @abstractmethod
    def create_transport(self):
        """This is the factory method"""
        pass

    def plan_delivery(self) -> str:
        # call fabric method `create_transport` to get transport instance
        transport = self.create_transport()
        result = f"Creator: The same creator's code has just worked with {transport.deliver()}"

        return result


class RoadLogistic(Logistic):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistic(Logistic):
    def create_transport(self) -> Transport:
        return Ship()


class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass


class Ship(Transport):
    def deliver(self) -> str:
        return "Be ready for the storms, we just started"


class Truck(Transport):
    def deliver(self) -> str:
        return "Our truck is the king of the road, we will be just in time"


def client_code(logistic: Logistic) -> None:
    print(f"Client: I'm not aware of the logistic's class, but it still works.\n"
          f"{logistic.plan_delivery()}", end="")


if __name__ == "__main__":
    print("App: Launched with the RoadLogistic.")
    client_code(RoadLogistic())
    print("\n")

    print("App: Launched with the SeaLogistic.")
    client_code(SeaLogistic())
