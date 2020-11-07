# async_logging

An experiment in Python multiprocessing and multithreading. A number of independent processes sending data to their stdout at a given frequency talks to a reader thread in a main application.  Each process has its own reader and its own list for arriving data. 

Oct 23rd 2020
Added a github action that runs flake, pytest, generates some html documentation and finally runs the main program logger.py 

CPython is the most popular implementation of the Python programming language. It is also a reference with more than 10000 committed changes by Guido van Rossum himself, the inventor of the language.