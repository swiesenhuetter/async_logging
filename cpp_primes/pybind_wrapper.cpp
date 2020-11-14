#include <pybind11/pybind11.h>
#include "primes.h"

bool cpp_is_prime(uint64_t n)
{
    auto result = primes::is_prime(n);
    return result;
}

bool cpp_is_prime_2core(uint64_t n)
{
    auto result = primes::is_prime_par(n);
    return result;
}

PYBIND11_MODULE(cpp_primes, m) {
    m.doc() = "Stephan Wiesenhuetter cpp experiment"; // Optional module docstring
    m.def("cpp_is_prime", &cpp_is_prime, "prime number check");
    m.def("cpp_is_prime_2core", &cpp_is_prime_2core, "prime number check parallel");
}
