# test/test_stats.py
from pytest import raises
from ..stats import DataCapture


class TestDataCapture:

    def test_datacapture_empty(self):
        """ Test constructs stats from an empty collection."""
        capture = DataCapture()
        stats = capture.build_stats()
        assert stats.greater(10) == 0
        assert stats.between(1, 1000) == 0
        assert stats.less(999) == 0

    def test_datacapture_simple_add(self):
        """ Test
        - add a number.
        - Less than the first
        - Greater than greatest
        - Between same number
        """
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

    def test_between_invalid_range(self):
        """ Between left greater then right. It must failed.
        """
        capture = DataCapture(1, 10, 100)
        stats = capture.build_stats()
        with raises(AssertionError):
            stats.between(100, 1)

    def test_input_for_values_never_added_before(self):
        """Test inputs, numbers never captured."""
        capture = DataCapture(1, 3, 5)
        stats = capture.build_stats()
        assert stats.less(6) == 3
        assert stats.greater(6) == 0
        assert stats.between(8, 9) == 0
        assert stats.greater(1000) == 0
        assert stats.between(2, 6) == 2

