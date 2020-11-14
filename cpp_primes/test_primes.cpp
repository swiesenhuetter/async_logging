#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "primes.h"
#include <numeric>

using namespace primes;

TEST_CASE("Prime-Test some numbers", "[primes]")
{

    REQUIRE(is_prime(2));
    REQUIRE(is_prime(31));
    REQUIRE_FALSE(is_prime(4));
    REQUIRE_FALSE(is_prime(100));
    REQUIRE(is_prime(101));
}

TEST_CASE("Prime-Test async a huge number", "[asyncprime]")
{
    auto t0 = ::GetTickCount();
    REQUIRE(is_prime(10657331232548839));
    auto dt1 = ::GetTickCount() - t0;

    t0 = ::GetTickCount();
    REQUIRE(is_prime_par(10657331232548839));
    auto dt2 = ::GetTickCount() - t0;
}

TEST_CASE("Prime-Test a huge number", "[bigprime]")
{
    REQUIRE(is_prime_par(10657331232548839));
}


TEST_CASE("Test split large range", "[split500]")
{
    std::vector<uint64_t> part_nums{ 1 , 2, 5, 10 };
    for (auto num_parts : part_nums)
    {
        auto result = split({ 500, 1000 }, num_parts);
        REQUIRE(num_parts == result.size());
        uint64_t sum{};
        for (const auto& r : result)
            sum += r.end - r.begin;
        REQUIRE(501 == sum);
    }
}

TEST_CASE("Test split small range", "[split]")
{
    Interval i{3, 7};
    auto result = split(i, 2);
    REQUIRE(2 == result.size());
    REQUIRE(3 == result.front().begin);
    REQUIRE(5 == result.front().end);
    REQUIRE(5 == result.back().begin);
    REQUIRE(8 == result.back().end);
}


