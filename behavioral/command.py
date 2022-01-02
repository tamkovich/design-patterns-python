from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict


class Command(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs) -> None:
        pass


class CopyCommand(Command):
    def execute(self, item: str) -> None:
        print(f"CopyCommand: '{item}' will be copied")


class DeleteCommand(Command):
    def __init__(self, receiver: DeleteReceiver) -> None:
        self._receiver = receiver

    def execute(self, item: str) -> None:
        self._receiver.do_something(item)


class DeleteReceiver:
    def do_something(self, item: str) -> None:
        print(f"DeleteReceiver: '{item}' will be deleted")


class Editor:
    """Invoker"""
    actions_map: Dict[str, Command] = {}

    def set_action(self, action_key: str, command: Command):
        self.actions_map[action_key] = command

    def execute(self, action_key: str, *args, **kwargs) -> None:
        self.actions_map[action_key].execute(*args, **kwargs)


if __name__ == "__main__":
    editor = Editor()
    copy_command = CopyCommand()
    receiver = DeleteReceiver()
    delete_command = DeleteCommand(receiver)
    editor.set_action('Ctrl+C', copy_command)
    editor.set_action('Del', delete_command)

    editor.execute('Del', 'my account')
    editor.execute('Ctrl+C', 'avatar')
    editor.execute('Ctrl+C', 'video')
