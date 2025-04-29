from typing import Iterable, Optional
from datastructures.ibag import IBag, T
from collections import Counter

class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.bag_dict = Counter()
        for item in items:
            if item is not None:
                self.bag_dict.update(item)

    def  add(self, item: T) -> None:
        self.bag_dict[item] += 1

    def remove(self, item: T) -> None:
        if self.bag_dict[item] > 0:
            self.bag_dict[item] -= 1
        if self.bag_dict[item] == 0:
            del self.bag_dict[item]

    def count(self, item: T) -> int:
        return self.bag_dict.get(item, 0)

    def __len__(self) -> int:
        return sum(self.bag_dict.values())

    def distinct_items(self) -> Iterable[T]:
        return self.bag_dict.keys()

    def __contains__(self, item) -> bool:
        return item in self.bag_dict

    def clear(self) -> None:
        self.bag_dict.clear()