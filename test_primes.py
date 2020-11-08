import primes as pr
import pytest


def test_range():
    found = pr.has_divisor(7, pr.Interval(3, 7))
    assert not found


def test_prime():
    assert pr.is_prime(2)
    assert pr.is_prime(31)
    assert not pr.is_prime(4)
    assert not pr.is_prime(100)
    assert pr.is_prime(101)


@pytest.fixture
def from_to():
    return pr.Interval(3, 11)


@pytest.mark.parametrize("part", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_partitions(from_to, part):
    result = pr.split(from_to, part)
    assert from_to.stop == (result[-1].stop - 1)


@pytest.mark.parametrize("parts", [1, 2, 5, 10])
def test_split_large(parts):
    result = pr.split(pr.Interval(500, 1000), parts)
    assert parts == len(result)
    sum_all = sum([i.stop - i.start for i in result])
    assert 501 == sum_all


def test_split(from_to):
    result = pr.split(from_to, 3)
    assert 3 == len(result)
    assert from_to.stop == (result[-1].stop - 1)


def test_huge_prime():
    number = 10657331232548839
    assert pr.is_prime(number)
