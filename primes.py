import math

from time import time
from functools import wraps
from collections import namedtuple


Interval = namedtuple('Interval', ['start', "stop"])


def timeit(func):
    """
    :param func: Decorated function
    :return: Execution time for the decorated function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'{func.__name__} executed in {end - start:.4f} seconds')
        return result
    return wrapper


@timeit
def has_divisor(n, search_interval):
    for divisor in range(search_interval.start, search_interval.stop, 2):
        if n % divisor == 0:
            print("{}/{}={}".format(n, divisor, n//divisor))
            return divisor
    return None


def split(interval, partitions):
    num_all = interval.stop - interval.start
    parts_size = round(num_all / partitions)
    starts = [par * parts_size + interval.start for par in range(partitions)]
    stops = [par * parts_size + parts_size + interval.start for par in range(partitions)]
    stops[-1] = interval.stop + 1
    return [Interval(start, stop) for start, stop in zip(starts, stops)]


@timeit
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    search_interval = Interval(start=3, stop=int(math.sqrt(n)) + 1)
    found_div = has_divisor(n, search_interval)
    if found_div:
        print("{}/{}={}".format(n, found_div, n//found_div))
        return False
    return True


if __name__ == "__main__":
    number = 10657331232548839
    is_prime(number)
    print("{} is prime".format(number))
