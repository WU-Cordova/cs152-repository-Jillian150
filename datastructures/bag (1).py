from typing import Iterable, Optional
from datastructures.ibag import IBag, T
from collections import Counter

class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.bag_dict: dict = True

    def add(self, item: T) -> None:
        self.add(item)
        Counter(self.bag_dict + 1)

    def remove(self, item: T) -> None:
        self.bag_dict.pop(item)
        Counter(self.bag_dict - 1)

    def count(self, item: T) -> int:
        raise NotImplementedError("count method not implemented")

    def __len__(self) -> int:
        raise NotImplementedError("__len__ method not implemented")

    def distinct_items(self) -> Iterable[T]:
        raise NotImplementedError("distinct_items method not implemented")

    def __contains__(self, item) -> bool:
        raise NotImplementedError("__contains__ method not implemented")

    def clear(self) -> None:
        raise NotImplementedError("clear method not implemented")