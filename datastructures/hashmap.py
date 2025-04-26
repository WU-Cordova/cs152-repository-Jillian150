import copy
from typing import Callable, Iterator, Optional, Tuple
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

from typing import Generic, TypeVar

KT = TypeVar("KT")  # Key type
VT = TypeVar("VT")  # Value type

class HashMap(Generic[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[int], int]] = None) -> None:
        self.number_of_buckets = number_of_buckets
        self.load_factor = load_factor
        self.custom_hash_function = custom_hash_function or self._default_hash_function
        self.buckets = [LinkedList() for _ in range(self.number_of_buckets)]
        self.size = 0

    @staticmethod
    def _default_hash_function(key) -> int:
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)

    def _get_bucket_index(self, key) -> int:
        return self.custom_hash_function(key) % self.number_of_buckets

    def _resize(self):
        if self.size / self.number_of_buckets > self.load_factor:
            old_buckets = self.buckets
            self.number_of_buckets *= 2
            self.buckets = [LinkedList() for _ in range(self.number_of_buckets)]
            self.size = 0

            for bucket in old_buckets:
                for node in bucket:
                    self.__setitem__(node.key, node.value)

    def __getitem__(self, key):
        index = self._get_bucket_index(key)
        bucket = self.buckets[index]
        for node in bucket:
            if node.key == key:
                return node.value
        raise KeyError(f"Key '{key}' not found")

    def __setitem__(self, key, value) -> None:
        index = self._get_bucket_index(key)
        bucket = self.buckets[index]
        for node in bucket:
            if node.key == key:
                node.value = value
                return
        bucket.append(key, value)
        self.size += 1
        self._resize()

    def keys(self) -> Iterator:
        for bucket in self.buckets:
            for node in bucket:
                yield node.key

    def values(self) -> Iterator:
        for bucket in self.buckets:
            for node in bucket:
                yield node.value

    def items(self) -> Iterator[Tuple]:
        for bucket in self.buckets:
            for node in bucket:
                yield (node.key, node.value)

    def __delitem__(self, key) -> None:
        index = self._get_bucket_index(key)
        bucket = self.buckets[index]
        for node in bucket:
            if node.key == key:
                bucket.remove(node)
                self.size -= 1
                return
        raise KeyError(f"Key '{key}' not found")

    def __contains__(self, key) -> bool:
        index = self._get_bucket_index(key)
        bucket = self.buckets[index]
        return any(node.key == key for node in bucket)

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator:
        return self.keys()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HashMap):
            return False
        return dict(self.items()) == dict(other.items())

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self.items()) + "}"

    def __repr__(self) -> str:
        return f"HashMap({str(self)})"