"""
Usage:
>>> capture = DataCapture(3, 9, 3, 4, 6)
>>> stats = capture.build_stats()
>>> stats.less(4) # should return 2 (only two values 3, 3 are less than 4)
2
>>> stats.between(3, 6) # should return 4 (3, 3, 4 and 6 are between 3 and 6)
4
>>> stats.greater(4) # should return 2 (6 and 9 are the only two values greater than 4)
2
"""
from collections import Counter
from bisect import bisect
from typing import List, Dict, Iterable
from functools import wraps


def validate_input(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        values = [*args, *kwargs.values()]
        for number in values:
            if not self._is_valid(number):
                raise ValueError('Invalid input number for stats: %r' % (number, ))
        return func(self, *args, **kwargs)

    return wrapper


class Stats:
    """ Gives simple stats of a collection of positive small integers."""
    MAX_INPUT = 1000

    def __init__(self, counts: Dict, sorted_keys: List[int]):
        self._less = dict()

        acum = 0
        for key in range(self.MAX_INPUT + 1):
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
        left must be less or equal to right
        """
        assert left <= right, 'Invalid range'
        return self._less[right] + self._counts[right] - self._less[left]

    @validate_input
    def greater(self, number: int) -> int:
        """ How many items are in the collection that are great than the input number.

        Requires input number must be part of the collection.
        """
        return self._total - self._less[number] - self._counts[number]

    def _is_valid(self, input):
        return isinstance(input, int) and input <= self.MAX_INPUT


class DataCapture(object):
    """ Captures the input and generate stats of small integers.

    """

    def __init__(self, *numbers: Iterable[int]) -> None:
        self._data = Counter()
        self._sorted_keys = list()
        self.add(*numbers)

    def add(self, *numbers: Iterable[int]):
        """ Add numbers to the data capture.
        """
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