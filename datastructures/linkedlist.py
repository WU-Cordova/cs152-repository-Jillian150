from __future__ import annotations
from dataclasses import dataclass
import os
from typing import Optional, Sequence, Iterator
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
        self.current: Optional[LinkedList.Node] = None
        self.count: int = 0
        self.data_type: type = data_type

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type = object) -> LinkedList[T]:
        ll = LinkedList(data_type)
        for item in sequence:
            ll.append(item)
        return ll

    def append(self, item: T) -> None:
        new_node = LinkedList.Node(item)
        if self.tail:
            self.tail.next = new_node
            new_node.previous = self.tail
        else:
            self.head = new_node
        self.tail = new_node
        self.count += 1

    def prepend(self, item: T) -> None:
        new_node = LinkedList.Node(item)
        if self.head:
            self.head.previous = new_node
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node
        self.count += 1

    def __iter__(self) -> Iterator[T]:
        self.current = self.head
        return self

    def __next__(self) -> T:
        if not self.current:
            raise StopIteration
        value = self.current.data
        self.current = self.current.next
        return value

    def __reversed__(self) -> Iterator[T]:
        current = self.tail
        while current:
            yield current.data
            current = current.previous
