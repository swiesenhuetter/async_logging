#include "primes.h"
#include <cmath>
#include <vector>
#include <future>

namespace primes {

    std::vector<Interval> split(Interval interval, uint64_t num_partitions)
    {
        std::vector<Interval> parts;
        if (num_partitions < 1) 
            return parts;

        auto num_all = interval.end - interval.begin;
        auto parts_size = static_cast<uint64_t>(round(num_all / num_partitions));
        for (int i = 0; i < num_partitions; ++i)
        {
            auto begin = i * parts_size + interval.begin;
            auto end = i * parts_size + parts_size + interval.begin;
            parts.push_back({ begin, end });
        }
        parts.back().end += 1;
        return parts;
    }

    EXPORT bool is_prime(uint64_t n)
    {
        if (n == 2)
            return true;
        if (n % 2 == 0 || n <=1 )
            return false;

        uint64_t test_until = static_cast<uint64_t>(sqrt(n));
        for (uint64_t divisor = 3; divisor <= test_until; divisor += 2)
            if (n % divisor == 0)
                return false;

        return true;
    }


    bool has_divisor(uint64_t n, Interval search_interval)
    {
        for (uint64_t divisor = search_interval.begin; divisor <= search_interval.end; divisor += 2)
            if (n % divisor == 0)
                return true;
        return false;
    }


    EXPORT bool is_prime_par(uint64_t n)
    {
        if (n == 2)
            return true;
        if (n % 2 == 0 || n <= 1)
            return false;
        uint64_t test_until = static_cast<uint64_t>(sqrt(n));
        Interval intvl{ 3, test_until };
        auto two_parts = split(intvl, 2);
        auto lower = std::async(std::launch::async, has_divisor, n, two_parts.front());
        auto upper = std::async(std::launch::async, has_divisor, n, two_parts.back());
        bool isprime = (!lower.get() && !upper.get());
        return isprime;
    }


}
