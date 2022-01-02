from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    _state = None

    def change_state(self, state: State) -> None:
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self


class AudioPlayer(Context):
    _state: State = None

    def __init__(self, state: State) -> None:
        self.change_state(state)

    def click_lock(self):
        print("Clicked lock")
        self._state.click_lock()
        print(f"Changed to {self._state}")

    def click_play(self):
        self._state.click_play()

    def click_next(self):
        self._state.click_next()

    def click_previous(self):
        self._state.click_previous()

    def start_playback(self):
        print("Started new song")

    def stop_playback(self):
        print("Stop music")

    def next_song(self):
        print("Changed to the next song")

    def previous_song(self):
        print("Changed to the previous song")

    @property
    def playing(self) -> bool:
        print("player is playing something")
        return True

    @property
    def doubleclick(self) -> bool:
        print("doubleclick event received")
        return True




class State(ABC):
    @property
    def player(self) -> Context:
        return self._player

    @player.setter
    def context(self, player: Context) -> None:
        self._player = player

    @abstractmethod
    def click_lock(self) -> None:
        pass

    @abstractmethod
    def click_play(self) -> None:
        pass

    @abstractmethod
    def click_next(self) -> None:
        pass

    @abstractmethod
    def click_previous(self) -> None:
        pass


class LockedState(State):
    def click_lock(self) -> None:
        if self.player.playing:
            self.player.change_state(PlayingState())
        else:
            self.player.change_state(ReadyState())

    def click_play(self) -> None:
        print("Do nothing")

    def click_next(self) -> None:
        print("Do nothing")

    def click_previous(self) -> None:
        print("Do nothing")


class PlayingState(State):
    def click_lock(self) -> None:
        self.player.change_state(LockedState())

    def click_play(self) -> None:
        self.player.stop_playback()
        self.player.change_state(ReadyState())

    def click_next(self) -> None:
        if self.player.doubleclick:
            self.player.next_song()
        else:
            self.player.fast_forward(5)

    def click_previous(self) -> None:
        if self.player.doubleclick:
            self.player.previous_song()
        else:
            self.player.rewind(5)


class ReadyState(State):
    '''
    method clickNext() is
        player.nextSong()

    method clickPrevious() is
        player.previousSong()
    '''
    def click_lock(self) -> None:
        self.player.change_state(LockedState())

    def click_play(self) -> None:
        self.player.start_playback()
        self.player.change_state(PlayingState())

    def click_next(self) -> None:
        self.player.next_song()

    def click_previous(self) -> None:
        self.player.previous_song()


if __name__ == "__main__":
    context = AudioPlayer(LockedState())
    print('\n')
    context.click_lock()
    print('\n')
    context.click_play()
    print('\n')
    context.click_next()
    print('\n')
    context.click_lock()
