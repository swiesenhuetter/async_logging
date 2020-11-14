#pragma once
#include <cmath>
#include <cstdint>
#include <vector>


// C - interface
#if defined (_MSC_VER)
    // MS Visual C++
    #define EXPORT __declspec(dllexport)
#elif defined (__GNUC__)
    //  GCC
    #define EXPORT __attribute__((visibility("default")))
#else
    //  do nothing and hope for the best?
    #define EXPORT
    #pragma warning Unknown dynamic link import/export semantics.
#endif


namespace primes
{
    struct Interval { uint64_t begin{}, end{}; };
    std::vector<Interval> split(Interval interval, uint64_t num_partitions);

    EXPORT bool is_prime(uint64_t n);

    EXPORT bool is_prime_par(uint64_t n);
}
