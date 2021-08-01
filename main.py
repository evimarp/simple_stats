from collections import Counter
from bisect import bisect
from typing import List, Dict, Iterable
from functools import wraps


def validate_input(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        values = [*args, *kwargs.values()]
        for number in values:
            if number not in self._less:
                raise ValueError('Invalid number for stats: %r' % (number, ))
        return func(self, *args, **kwargs)

    return wrapper


class Stats:
    """ Gives simple stats of a collection of positive small integers."""
    
    def __init__(self, counts: Dict, sorted_keys: List[int]):
        self._less = dict()

        acum = 0
        for key in sorted_keys:
            self._less[key] = acum
            acum += counts[key]
        self._total = acum
        self._counts = counts

    @validate_input
    def less(self, number: int) -> int:
        """ How many items are in the collection that are less than the input number.

        Requires input number must be part of the collection.
        """
        return self._less[number]

    @validate_input
    def between(self, left: int, right: int) -> int:
        """ How many items are in the collection that are between left and right numbers, both inclusive.

        Requires input numbers left and right must be part of the collection.
        """
        return self._less[right] + self._counts[right] - self._less[left]

    @validate_input
    def greater(self, number: int) -> int:
        """ How many items are in the collection that are great than the input number.

        Requires input number must be part of the collection.
        """
        return self._total - self._less[number] - self._counts[number]


class DataCapture(object):
    """ Captures the input and generate stats of small integers.

    >>> datacapture = DataCapture()
    >>> datacapture.add(10)
    >>> datacapture.add(1)
    >>> datacapture.add(5)
    >>> datacapture._sorted_keys
    [1, 5, 10]
    >>> datacapture.add(1)
    >>> datacapture._sorted_keys
    [1, 5, 10]
    >>> datacapture._data[1]
    2
    >>> datacapture._data[5]
    1
    >>> datacapture._data[8]
    0
    >>> stats = datacapture.build_stats()
    >>> stats.less(1)
    0
    """

    def __init__(self) -> None:
        self._data = Counter()
        self._sorted_keys = list()

    def add(self, *numbers: Iterable):
        self._data += Counter(numbers)
        for number in numbers:
            if number not in self._sorted_keys:
                index = bisect(self._sorted_keys, number)
                self._sorted_keys.insert(index, number)

    def build_stats(self) -> Stats:
        return Stats(self._data, self._sorted_keys)


if __name__ == '__main__':
    from doctest import testmod
    testmod()