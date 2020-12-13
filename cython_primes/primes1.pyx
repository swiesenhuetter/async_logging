import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    search_up_to = int(math.sqrt(n)) + 1
    for divisor in range(3, search_up_to, 2):
        if n % divisor == 0:
            print("{}/{}={}".format(n, divisor, n // divisor))
            return False
    return True


if __name__ == "__main__":
    number = 10657331232548839
    if is_prime(number):
        print("{} is prime".format(number))
