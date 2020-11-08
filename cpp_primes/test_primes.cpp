#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "primes.h"

using namespace primes;

TEST_CASE("Prime-Test some numbers", "[primes]")
{

    REQUIRE(is_prime(2));
    REQUIRE(is_prime(31));
    REQUIRE_FALSE(is_prime(4));
    REQUIRE_FALSE(is_prime(100));
    REQUIRE(is_prime(101));
}

TEST_CASE("Prime-Test a huge number", "[bigprime]")
{
    REQUIRE(is_prime(10657331232548839));
}

