import math

from time import time
from collections import namedtuple
from typing import NamedTuple

cimport cython


Interval = namedtuple('Interval', ['start', "stop"])


@cython.cdivision(True)
cdef unsigned long long has_divisor(unsigned long long n, search_interval):
    cdef unsigned long long divisor, start, stop
    start = search_interval.start
    stop = search_interval.stop
    for divisor in range(start, stop, 2):
        if n % divisor == 0:
            print("{}/{}={}".format(n, divisor, n//divisor))
            return divisor
    return 0


def is_prime(unsigned long long n):
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


def main():
    candidate_num = 10657331232548839
    start = time()
    is_prime(candidate_num)
    end = time()
    print("{} is prime".format(candidate_num))
    print(f'is_prime executed in {end - start:.4f} seconds')

if __name__ == "__main__":
    main()