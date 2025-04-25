from __future__ import annotations
from typing import Generic, TypeVar, Optional
from datastructures.linkedlist import LinkedList

T = TypeVar("T")

class ListStack(Generic[T]):
    def __init__(self, data_type: type) -> None:
        """Initializes the ListStack using LinkedList."""
        self._list = LinkedList[T](data_type)

    def push(self, item: T):
        """Pushes an item onto the stack."""
        self._list.prepend(item)

    def pop(self) -> T:
        """Removes and returns the top item from the stack."""
        if self.empty:
            raise IndexError("Pop from an empty stack")
        return self._list.pop_front()

    def peek(self) -> T:
        """Returns the top item from the stack without removing it."""
        if self.empty:
            raise IndexError("Peek from an empty stack")
        return self._list.front

    @property
    def empty(self) -> bool:
        """Checks if the stack is empty."""
        return self._list.empty

    def clear(self):
        """Clears all items from the stack."""
        self._list.clear()

    def __contains__(self, item: T) -> bool:
        """Checks if an item exists in the stack."""
        return item in self._list

    def __eq__(self, other: object) -> bool:
        """Compares two stacks for equality."""
        if not isinstance(other, ListStack):
            return False
        return self._list == other._list

    def __len__(self) -> int:
        """Returns the number of items in the stack."""
        return len(self._list)

    def __str__(self) -> str:
        """Returns a string representation of the stack."""
        return str(self._list)

    def __repr__(self) -> str:
        """Returns a detailed string representation of the stack."""
        return f"ListStack({repr(self._list)})"