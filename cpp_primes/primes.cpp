#include "primes.h"
#include <cmath>

namespace primes {
    EXPORT bool is_prime(uint64_t n)
    {
        if (n == 2)
            return true;
        if (n % 2 == 0 || n <=1 )
            return false;

        uint64_t test_until = static_cast<uint64_t>(sqrt<uint64_t>(n));
        for (uint64_t divisor = 3; divisor <= test_until; divisor += 2)
            if (n % divisor == 0)
                return false;

        return true;
    }
}
