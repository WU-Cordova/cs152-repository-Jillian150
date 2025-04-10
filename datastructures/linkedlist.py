from __future__ import annotations
from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.count: int = 0
        self.data_type: type = data_type

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type = object) -> LinkedList[T]:
        ll = LinkedList(data_type)
        for item in sequence:
            ll.append(item)
        return ll

    def append(self, item: T) -> None:
        self._check_type(item)
        new_node = LinkedList.Node(item)
        if self.tail:
            self.tail.next = new_node
            new_node.previous = self.tail
        else:
            self.head = new_node
        self.tail = new_node
        self.count += 1

    def prepend(self, item: T) -> None:
        self._check_type(item)
        new_node = LinkedList.Node(item)
        if self.head:
            self.head.previous = new_node
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node
        self.count += 1

    def insert_before(self, target: T, item: T) -> None:
        self._check_type(item)
        current = self.head
        while current:
            if current.data == target:
                new_node = LinkedList.Node(item, next=current, previous=current.previous)
                if current.previous:
                    current.previous.next = new_node
                else:
                    self.head = new_node
                current.previous = new_node
                self.count += 1
                return
            current = current.next
        raise ValueError(f"Target {target} not found in the list.")

    def insert_after(self, target: T, item: T) -> None:
        self._check_type(item)
        current = self.head
        while current:
            if current.data == target:
                new_node = LinkedList.Node(item, previous=current, next=current.next)
                if current.next:
                    current.next.previous = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                self.count += 1
                return
            current = current.next
        raise ValueError(f"Target {target} not found in the list.")

    def remove(self, item: T) -> None:
        current = self.head
        while current:
            if current.data == item:
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                self.count -= 1
                return
            current = current.next
        raise ValueError(f"Item {item} not found in the list.")

    def remove_all(self, item: T) -> None:
        current = self.head
        while current:
            if current.data == item:
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                self.count -= 1
            current = current.next

    def pop(self) -> T:
        if not self.tail:
            raise IndexError("Pop from empty list")
        value = self.tail.data
        if self.tail.previous:
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            self.head = self.tail = None
        self.count -= 1
        return value

    def pop_front(self) -> T:
        if not self.head:
            raise IndexError("Pop from empty list")
        value = self.head.data
        if self.head.next:
            self.head = self.head.next
            self.head.previous = None
        else:
            self.head = self.tail = None
        self.count -= 1
        return value

    @property
    def front(self) -> T:
        if not self.head:
            raise IndexError("Front from empty list")
        return self.head.data

    @property
    def back(self) -> T:
        if not self.tail:
            raise IndexError("Back from empty list")
        return self.tail.data

    @property
    def empty(self) -> bool:
        return self.count == 0

    def __len__(self) -> int:
        return self.count

    def __contains__(self, item: T) -> bool:
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def clear(self) -> None:
        self.head = self.tail = None
        self.count = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __reversed__(self):
        current = self.tail
        while current:
            yield current.data
            current = current.previous

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        return list(self) == list(other)

    def _check_type(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item {item} must be of type {self.data_type}")

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')