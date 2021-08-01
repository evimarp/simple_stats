# test/test_stats.py
from ..stats import DataCapture


class TestDataCapture:

    def test_datacapture_empty(self):
        """ Test constructs stats from an empty collection."""
        capture = DataCapture()
        stats = capture.build_stats()

    def test_datacapture_simple_add(self):
        """ Test
        - add a number.
        - Less than the first
        - Greater than greatest """
        capture = DataCapture()
        capture.add(3)
        capture.add(6)
        capture.add(4)
        capture.add(9)
        capture.add(3)
        stats = capture.build_stats()
        assert stats.less(3) == 0
        assert stats.greater(9) == 0
        assert stats.between(3, 3) == 2

    def test_datacapture_add_list(self):
        """ Test
        - add a list of numbers
        - less a number in the middle
        - greater a number in the middle
        - between all items on the collection
        """
        capture = DataCapture()
        primes = [1, 2, 3, 5, 7, 11, 13]
        capture.add(*primes)
        stats = capture.build_stats()
        assert stats.less(3) == 2
        assert stats.greater(11) == 1
        assert stats.between(1, 13) == 7

    def test_datacapture_adding_combination(self):
        """ Test
        - add at inizialization
        - add from a set
        - adding repeat numbers
        - less a number in the middle
        - greater a number in the middle
        - between not all items on the collection
        """
        capture = DataCapture(1, 10, 100)
        primes = {1, 2, 3, 5, 7, 11, 13}
        capture.add(*primes)
        stats = capture.build_stats()
        assert stats.less(3) == 3
        assert stats.greater(11) == 2
        assert stats.between(1, 13) == 9

