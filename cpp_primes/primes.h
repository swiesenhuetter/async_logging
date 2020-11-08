#pragma once
#include <cmath>
#include <cstdint>


// C - interface
#define PRIMES_API extern "C" __declspec(dllexport)

namespace primes
{
    PRIMES_API bool is_prime(uint64_t n);
}
