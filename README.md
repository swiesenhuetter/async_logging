# async_logging

An experiment in Python multiprocessing and multithreading. A number of independent processes sending data to their stdout at a given frequency talks to a reader thread in a main application.  Each process has its own reader and its own list for incoming data. 

Oct 23rd 2020
Added a github action that runs flake, pytest, generates some html documentation and finally runs the main program logger.py 

Nov 8th 2020 
Explore async processing and compare speed to c++

Asynchronous processing happens when two or more actions are executed in overlapping time intervals. The classic scenario is a process waiting for a slow I/O operation to finish. While this process needs to wait, it has no use for the CPU. It would still be desirable to use the CPU for another process or for handling user input and to draw screen content in a GUI thread. Python has the asyncio core library for asynchronous input and output since version 3.3. 

Parallel processing, in contrast, means that two or more actions are running on n processing units at the same time. This can result in a theoretical speed improvement from n down to 1/n runtime. This performance improvement can only be achieved if there are at least n independent processing units and the task can be split into n non-interacting and parts. 

The elegance of Python is a result of abstractions and it comes at a price. Details of memory handling, CPU architecture and other machine aspects are not mixed up with program logic. The result is that memory and runtime performance are not ideal in certain situations. CPython, the reference implementation of the language does not support parallel execution of multiple threads. Its interpreter has a global lock that can be acquired by only one thread at a time. This simplifies the CPython implementation because without the global interpreter lock (the GIL), all data structures and functions would have to be made thread safe, which would complicate them a lot. That means that CPython is not the right tool for distributing CPU intensive tasks across multiple cores. Another issue is the execution speed. It is restricted by translating the statements at runtime in the interpreter and by side effects of dynamic typing. Each object carries its type information which needs space and time when it is stored and evaluated. 

The intended audience for this article is the Python programmer who has hit those limitations in pure Python. If you have never used compiled and statically typed programming languages, you will benefit from reading any introductory material on C++ or C and from trying a few simple examples.Large-scale software design patterns and architecture considerations can be ignored at this moment as we will only apply those tools selectively and locally to treat just the performance bottlenecks we have identified.   
 
I will demonstrate two methods to improve on parallelism and on execution speed. Both make use on the efficiency of C and C++. The design of those languages was guided by the Zero-overhead principle which states that: 
 * You should not have to pay for something you don't use
 * Using language features is better than implementing them yourself 
 
 ## Cython
 Cython is an implementation of the Python language. Actually, it is a superset of the language because it has some C-inspired features while it also accepts unmodified Python programs. Cython compiles this code to C which is then compiled to machine instructions in a second step. It is used to create modules which can be imported and called from interpreted Python. Simply get it from PyPI, the Python Package index, by running ```pip install Cython```
 
 To illustrate the possible performance gains, I chose a prime number test. This test is a function that takes a number and returns a boolean value. The return value is `True` if the number is prime or `False` if it has a divisor. This example is simple but it shows a noticeable delay when  large prime numbers `n` are tested and no divisor candidate divides `n`. 
 ### The pure Python version
 ``` python
def has_divisor(n, search_interval):
    for divisor in range(search_interval.start, search_interval.stop, 2):
        if n % divisor == 0:
            print("{}/{}={}".format(n, divisor, n//divisor))
            return divisor
    return None

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    search_interval = Interval(start=3, stop=int(math.sqrt(n)) + 1)
    found_div = has_divisor(n, search_interval)
    if found_div:
        print("{}/{}={}".format(n, found_div, n//found_div))
        return False
    return True
``` 
for a large prime number such as 10657331232548839 `is_prime(10657331232548839)` will run several seconds. This number is so big, that 64 bit integer is needed to encode it.
