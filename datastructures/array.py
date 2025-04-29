# datastructures.array.Array


""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray



from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        self._logical_size: int = len(starting_sequence)
        self._physical_size: int = self._logical_size
        self._data_type: type = data_type

        if not isinstance(starting_sequence, Sequence):
            raise ValueError('starting_sequence must be a valid sequence type')
        
        for index in range(self._logical_size):
            if not isinstance(starting_sequence[index], self._data_type):
                raise TypeError('Items in starting sequence are not all the same type')
            
        self._items: NDArray = np.empty(self._physical_size, dtype=self._data_type)

        for index in range(self._logical_size):
            self._items[index] = starting_sequence[index]

        raise NotImplementedError('Constructor not implemented.')

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, int):
            if index < 0 or index >= self._logical_size:
                raise IndexError('Index out of range')
            return self._items[index]
        elif isinstance(index, slice):
            return self._items[index.start:index.stop:index.step]
        else:
            raise TypeError('Invalid argument type')

    def __setitem__(self, index: int, item: T) -> None:
        if index < 0 or index >= self._logical_size:
            raise IndexError('Index out of range')
        self._items[index] = item

    def append(self, data: T) -> None:
        if self._logical_size >= self._physical_size:
            self._resize()
        self._items[self._logical_size] = data
        self._logical_size += 1

    def append_front(self, data: T) -> None:
        if self._logical_size >= self._physical_size:
            self._resize()
        self._items[1:self._logical_size+1] = self._items[0:self._logical_size]
        self._items[0] = data
        self._logical_size += 1

    def pop(self) -> T:
        if self._logical_size == 0:
            raise IndexError('Pop from empty array')
        value = self._items[self._logical_size - 1]
        self._logical_size -= 1
        return value
    
    def pop_front(self) -> T:
        if self._logical_size == 0:
            raise IndexError('Pop from empty array')
        value = self._items[0]
        self._items[0:self._logical_size-1] = self._items[1:self._logical_size]
        self._logical_size -= 1
        return value

    def __len__(self) -> int: 
        return self._logical_size

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Array):
            return NotImplemented
        if self._logical_size != other._logical_size:
            return False
        return all(self._items[i] == other._items[i] for i in range(self._logical_size))
    
    def __iter__(self) -> Iterator[T]:
        return iter(self._items[:self._logical_size])

    def __reversed__(self) -> Iterator[T]:
        return reversed(self._items[:self._logical_size])

    def __delitem__(self, index: int) -> None:
        if index < 0 or index >= self._logical_size:
            raise IndexError('Index out of range')
        self._items[index:self._logical_size-1] = self._items[index+1:self._logical_size]
        self._logical_size -= 1

    def __contains__(self, item: Any) -> bool:
        return item in self._items[:self._logical_size]

    def clear(self) -> None:
        self._logical_size = 0

    def _resize(self) -> None:
        self._physical_size *= 2
        new_items = np.empty(self._physical_size, dtype=self._data_type)
        new_items[:self._logical_size] = self._items
        self._items = new_items

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self._items[:self._logical_size]) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self._logical_size}, Physical: {len(self._items)}, type: {self._data_type}'

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
