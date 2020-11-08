cpp#include <pybind11/pybind11.h>
#include "primes.h"

bool cpp_is_prime(uint64_t n)
{
    auto result = primes::is_prime(n);
    return result;
}

PYBIND11_MODULE(cpp_primes, m) {
    m.doc() = "Stephan Wiesenhuetter cpp experiment"; // Optional module docstring
    m.def("cpp_is_prime", &cpp_is_prime, "prime number check");
}
