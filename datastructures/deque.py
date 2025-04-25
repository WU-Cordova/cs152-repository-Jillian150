from __future__ import annotations
from typing import Optional, TypeVar, Generic, Sequence

T = TypeVar('T')

class LinkedList(Generic[T]):
    class Node:
        def __init__(self, data: T, next: Optional[LinkedList.Node] = None, previous: Optional[LinkedList.Node] = None) -> None:
            self.data = data
            self.next = next
            self.previous = previous

    def __init__(self) -> None:
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.count = 0

    def append(self, item: T) -> None:
        """Adds an item to the end of the list."""
        new_node = self.Node(item)
        if self.tail:
            self.tail.next = new_node
            new_node.previous = self.tail
        else:
            self.head = new_node
        self.tail = new_node
        self.count += 1

    def prepend(self, item: T) -> None:
        """Adds an item to the beginning of the list."""
        new_node = self.Node(item)
        if self.head:
            self.head.previous = new_node
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node
        self.count += 1

    def pop(self) -> T:
        """Removes and returns the last item in the list."""
        if not self.tail:
            raise IndexError("List is empty")
        value = self.tail.data
        self.tail = self.tail.previous
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.count -= 1
        return value

    def pop_front(self) -> T:
        """Removes and returns the first item in the list."""
        if not self.head:
            raise IndexError("List is empty")
        value = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.previous = None
        else:
            self.tail = None
        self.count -= 1
        return value

    @property
    def front(self) -> T:
        """Returns the first item in the list."""
        if not self.head:
            raise IndexError("List is empty")
        return self.head.data

    @property
    def back(self) -> T:
        """Returns the last item in the list."""
        if not self.tail:
            raise IndexError("List is empty")
        return self.tail.data

    def __len__(self) -> int:
        """Returns the number of items in the list."""
        return self.count

    def __contains__(self, item: T) -> bool:
        """Checks if an item exists in the list."""
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def clear(self) -> None:
        """Clears all items from the list."""
        self.head = None
        self.tail = None
        self.count = 0

    def __iter__(self):
        """Returns an iterator over the list."""
        self._current = self.head
        return self

    def __next__(self) -> T:
        """Returns the next item in the iteration."""
        if self._current:
            data = self._current.data
            self._current = self._current.next
            return data
        else:
            raise StopIteration

    def __str__(self) -> str:
        """Returns a string representation of the list."""
        values = []
        current = self.head
        while current:
            values.append(repr(current.data))
            current = current.next
        return '[' + ' <-> '.join(values) + ']'