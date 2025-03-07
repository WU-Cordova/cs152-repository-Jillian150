from __future__ import annotations
import os
from typing import Iterator, Sequence, TypeVar

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T

T = TypeVar('T')

class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int) -> None:
            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns

        def __getitem__(self, column_index: int) -> T:
            return self.array[self.row_index][column_index]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            self.array[self.row_index][column_index] = value
        
        def __iter__(self) -> Iterator[T]:
            return iter(self.array[self.row_index])
        
        def __reversed__(self) -> Iterator[T]:
            return reversed(self.array[self.row_index])

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        self._data = [list(row) for row in starting_sequence]
        self.__num_rows = len(self._data)
        self.__num_columns = len(self._data[0]) if self.__num_rows > 0 else 0

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        return Array2D([[data_type() for _ in range(cols)] for _ in range(rows)], data_type)

    def __getitem__(self, row_index: int) -> Array2D.Row[T]: 
        return Array2D.Row(row_index, self._data, self.__num_columns)
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        return iter(self._data)
    
    def __reversed__(self) -> Iterator[Sequence[T]]:
        return reversed(self._data)
    
    def __len__(self) -> int: 
        return self.__num_rows
    
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__num_rows} Rows x {self.__num_columns} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
