# async_logging

An experiment in Python multiprocessing and multithreading. A number of independent processes sending data to their stdout at a given frequency talks to a reader thread in a main application.  Each process has its own reader and its own list for arriving data. 

Oct 23rd 2020
Added a github action that runs flake, pytest and the main program logger.py
