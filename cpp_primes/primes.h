#pragma once
#include <cmath>
#include <cstdint>


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
    EXPORT bool is_prime(uint64_t n);
}
