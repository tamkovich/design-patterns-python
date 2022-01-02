from __future__ import annotations

import enum
from abc import ABC
from typing import List


class State(enum.Enum):
    AIR = 1
    RUNWAY = 2
    GARAGE = 3
    LANDING_STRIP = 4


class Mediator(ABC):
    def notify(self, sender: object, event: State) -> None:
        pass


class AirportDispatcher(Mediator):
    def __init__(self, machines: List[BaseMachine]) -> None:
        self._machines = machines
        for machine in self._machines:
            machine.mediator = self

    def notify(self, machine: BaseMachine, event: State) -> None:
        if event == State.LANDING_STRIP:
            decline_state = State.RUNWAY
        elif event == State.RUNWAY:
            decline_state = State.LANDING_STRIP
        if any([m.state == decline_state for m in self._machines]):
            print(f'Decline request for {machine}')
        else:
            print(f'Approve request for {machine}')
            machine.state = event


class BaseComponent:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class BaseMachine(BaseComponent):
    state: State = None

    def landing(self) -> None:
        print(f"{self.__class__.__name__} wanna go down")
        self.mediator.notify(self, State.LANDING_STRIP)

    def takeoff(self) -> None:
        print(f"{self.__class__.__name__} wanna takeoff")
        self.mediator.notify(self, State.RUNWAY)


class Boeing747(BaseMachine):
    pass


class Helicopter(BaseMachine):
    pass


if __name__ == "__main__":
    boeing = Boeing747()
    boeing.state = State.AIR
    helicopter = Helicopter()
    helicopter.state = State.GARAGE
    mediator = AirportDispatcher([boeing, helicopter])

    boeing.landing()

    print("\n", end="")

    helicopter.takeoff()
