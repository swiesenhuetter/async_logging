# async_logging

An experiment in Python multiprocessing and multithreading. A number of independent processes sending data to their stdout at a given frequency talks to a reader thread in a main application.  Each process has its own reader and its own list for incoming data. 

Oct 23rd 2020
Added a github action that runs flake, pytest, generates some html documentation and finally runs the main program logger.py 

Nov 8th 2020 
Explore async processing and compare speed to c++

Asynchronous processing happens when two or more actions are executed in overlapping time intervals. The classic scenario is a process waiting for a slow I/O operation to finish. While this process needs to wait, it has no use for the CPU. It would still be desirable to use the CPU for another process or for handling user input and to draw screen content in a GUI thread.

Parallel processing, in contrast, means that two ore more actions are running on n processing units at the same time. This can result in a theoretical speed improvement from n down to 1/n runtime. This performance improvemnt can only be achieved if there are at least n independent processing units and the task can be split into n parts completely independent of each other. 

Python has a core library for asynchronous input and output since version 3.3. CPython is the most popular implementation of the Python programming language. It is also a reference with more than 10000 committed changes by Guido van Rossum himself, the inventor of the language. 