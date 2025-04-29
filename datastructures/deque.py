from typing import TypeVar, Generic
from datastructures.linkedlist import LinkedList

T = TypeVar("T")

class Deque(Generic[T]):
    def __init__(self, data_type: type = object) -> None:
        """Initializes an empty deque using LinkedList."""
        self._list = LinkedList[T](data_type)

    def enqueue(self, item: T) -> None:
        """Adds an item to the back of the deque."""
        self._list.append(item)

    def enqueue_front(self, item: T) -> None:
        """Adds an item to the front of the deque."""
        self._list.prepend(item)

    def dequeue(self) -> T:
        """Removes and returns the first item in the deque."""
        if self.empty:
            raise IndexError("Dequeue from an empty deque")
        return self._list.pop_front()

    def dequeue_back(self) -> T:
        """Removes and returns the last item in the deque."""
        if self.empty:
            raise IndexError("Dequeue from an empty deque")
        return self._list.pop()

    @property
    def front(self) -> T:
        """Returns the first item in the deque."""
        if self.empty:
            raise IndexError("Front from an empty deque")
        return self._list.front

    @property
    def back(self) -> T:
        """Returns the last item in the deque."""
        if self.empty:
            raise IndexError("Back from an empty deque")
        return self._list.back

    @property
    def empty(self) -> bool:
        """Checks if the deque is empty."""
        return self._list.empty

    def __len__(self) -> int:
        """Returns the number of items in the deque."""
        return len(self._list)

    def __contains__(self, item: T) -> bool:
        """Checks if an item exists in the deque."""
        return item in self._list

    def clear(self) -> None:
        """Clears all items from the deque."""
        self._list.clear()

    def __iter__(self):
        """Returns an iterator over the deque."""
        return iter(self._list)

    def __str__(self) -> str:
        """Returns a string representation of the deque."""
        return str(self._list)

    def __repr__(self) -> str:
        """Returns a detailed string representation of the deque."""
        return f"Deque({repr(self._list)})"