from __future__ import annotations

import random
from collections.abc import Iterable, Iterator
from typing import Any, List, ClassVar


class AlphabeticalOrderIterator(Iterator):
    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class RandomIterator(Iterator):
    _count = 0

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection

    def __next__(self):
        self._count += 1
        if self._count > len(self._collection):
            raise StopIteration()
        return random.choice(self._collection)


class WordsCollection(Iterable):
    def __init__(self, iterator_class: ClassVar[Iterator], collection: List[Any]) -> None:
        self._iterator_class = iterator_class
        self._collection = collection

    def __iter__(self) -> Iterator:
        return self._iterator_class(self._collection)

    def get_reverse_iterator(self) -> Iterator:
        return self._iterator_class(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection(iterator_class=AlphabeticalOrderIterator, collection=[])
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")

    print("\n\nForloop traversal:")
    for i in collection:
        print(i)

    random_collection = WordsCollection(iterator_class=RandomIterator, collection=[])
    random_collection.add_item("First")
    random_collection.add_item("Second")
    random_collection.add_item("Third")

    print("\nRandom traversal:")
    print("\n".join(random_collection))
