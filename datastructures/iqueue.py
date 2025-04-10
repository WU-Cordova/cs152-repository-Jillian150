from abc import abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')

class IQueue(Generic[T]):
    ''' Interface for a queue data structure '''

    @abstractmethod
    def enqueue(self, item: T) -> None:
        ''' Enqueues an item into the queue.
        
            Arguments:
                item: T -- The item to enqueue.
        '''
        pass

    @abstractmethod
    def dequeue(self) -> T:
        ''' Dequeues an item from the queue.
        
            Returns:
                T -- The item dequeued from the queue.
        '''
        pass

    @abstractmethod
    def front(self) -> T:
        ''' Returns the front item in the queue without removing it.
        
            Returns:
                T -- The front item in the queue.
        '''
        pass

    @abstractmethod
    def back(self) -> T:
        ''' Returns the back item in the queue without removing it.
        
            Returns:
                T -- The back item in the queue.
        '''
        pass

    @abstractmethod
    def __len__(self) -> int:
        ''' Returns the number of items in the queue.   
        
            Returns:
                int -- The number of items in the queue.
        '''
        pass

    @abstractmethod
    def empty(self) -> bool:
        ''' Returns True if the queue is empty, False otherwise. 
        
            Returns:
                bool: True if the queue is empty, False otherwise.
        '''
        pass

    @abstractmethod
    def clear(self) -> None:
        ''' Clears the queue. '''
        pass

    @abstractmethod
    def __contains__(self, item: T) -> bool:
        ''' Returns True if the item is in the queue, False otherwise.
        
            Arguments:
                item: T -- The item to search for.
                
            Returns:
                bool: True if the item is in the queue, False otherwise.
        '''
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        ''' Compares two queues for equality.
        
            Arguments:
                other: object -- The other queue to compare.
                
            Returns:
                bool -- True if the queues are equal, False otherwise.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        ''' Returns a string representation of the queue.
        
            Returns:
                str -- A string representation of the queue.
        '''
        pass

    @abstractmethod
    def __repr__(self) -> str:
        ''' Returns a string representation of the queue.
        
            Returns:
                str -- A string representation of the queue.
        '''
        pass


class Queue(IQueue[T]):
    ''' Implementation of a queue data structure '''

    def __init__(self) -> None:
        self._items: List[T] = []

    def enqueue(self, item: T) -> None:
        ''' Enqueues an item into the queue.
        
            Arguments:
                item: T -- The item to enqueue.
        '''
        self._items.append(item)

    def dequeue(self) -> T:
        ''' Dequeues an item from the queue.
        
            Returns:
                T -- The item dequeued from the queue.
        '''
        if not self._items:
            raise IndexError("Dequeue from an empty queue.")
        return self._items.pop(0)

    def front(self) -> T:
        ''' Returns the front item in the queue without removing it.
        
            Returns:
                T -- The front item in the queue.
        '''
        if not self._items:
            raise IndexError("Accessing front in an empty queue.")
        return self._items[0]

    def back(self) -> T:
        ''' Returns the back item in the queue without removing it.
        
            Returns:
                T -- The back item in the queue.
        '''
        if not self._items:
            raise IndexError("Accessing back in an empty queue.")
        return self._items[-1]

    def __len__(self) -> int:
        ''' Returns the number of items in the queue.   
        
            Returns:
                int -- The number of items in the queue.
        '''
        return len(self._items)

    def empty(self) -> bool:
        ''' Returns True if the queue is empty, False otherwise. 
        
            Returns:
                bool: True if the queue is empty, False otherwise.
        '''
        return len(self._items) == 0

    def clear(self) -> None:
        ''' Clears the queue. '''
        self._items.clear()

    def __contains__(self, item: T) -> bool:
        ''' Returns True if the item is in the queue, False otherwise.
        
            Arguments:
                item: T -- The item to search for.
                
            Returns:
                bool: True if the item is in the queue, False otherwise.
        '''
        return item in self._items

    def __eq__(self, other: object) -> bool:
        ''' Compares two queues for equality.
        
            Arguments:
                other: object -- The other queue to compare.
                
            Returns:
                bool -- True if the queues are equal, False otherwise.
        '''
        if not isinstance(other, Queue):
            return False
        return self._items == other._items

    def __str__(self) -> str:
        ''' Returns a string representation of the queue.
        
            Returns:
                str -- A string representation of the queue.
        '''
        return f"Queue({self._items})"

    def __repr__(self) -> str:
        ''' Returns a string representation of the queue.
        
            Returns:
                str -- A string representation of the queue.
        '''
        return self.__str__()