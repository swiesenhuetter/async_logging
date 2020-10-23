import sys
from subprocess import Popen, PIPE
import threading
import re
import signal


def start_proc(interval):
    """
    Start Python interpreter process executing sender.py, given a wait interval
    """
    pipe = Popen([sys.executable, 'sender.py', str(interval)], stdout=PIPE)
    return pipe


def parse_line(log_msg):
    """
    Extract a pair of two integers from a message string or
    None if log_msg does not contain exactly 2 (int) numbers
    """
    p = re.compile(r'\d+')
    num_pair = p.findall(log_msg)
    num_pair = [int(n) for n in num_pair]  # list of numbers as text to integers
    if len(num_pair) == 2:
        return num_pair
    else:
        return None


def stream_reader(pipe, log_data):
    """
    IO pipe from another process receives the stdout text
    parse number pair clock and process ID and append to log
    readline() blocks until a line arrives
    when length reaches 10 stop the process (kill call)
    """
    msg = 'Thread {} started'.format(threading.get_ident())
    print(msg)
    while True:
        text = pipe.stdout.readline()
        print(text)
        clock, proc_id = parse_line(str(text))
        log_data.append((clock, proc_id))
        if len(log_data) >= 10:
            print("10 reached")
            pipe.kill()
            return


"""list of intervals in seconds"""
time_intervals = [0.2, 0.1, 1, 0.01]  # simulate async devices
"""for each interval entry start a separate process"""
pipes = [start_proc(interval) for interval in time_intervals]
receive_data = []
threads = []


for i in range(len(pipes)):
    """
    for each process start a reader thread 
    """
    receive_data.append([])
    t = threading.Thread(target=stream_reader, args=(pipes[i], receive_data[i]))
    t.start()
    threads.append(t)

[t.join() for t in threads]
table = list(zip(*receive_data))  # transpose list of lists

[print(line) for line in table]   # by device

all_events = []
"""one column per process"""
[all_events.extend(col) for col in receive_data]
"""one line per event"""
all_events = (sorted(all_events, key=lambda x: x[0]))  # all events on the same time axis
[print(line) for line in all_events]   # by device

