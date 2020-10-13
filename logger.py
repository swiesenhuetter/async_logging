import sys
import subprocess as proc
import threading
import re

time_intervals = [0.001, 0.9, 0.2, 0.1]  # simulate async devices


def start_proc(interval):
    pipe = proc.Popen([sys.executable, 'sender.py', str(interval)], stdout=proc.PIPE)
    return pipe


pipes = [start_proc(i) for i in time_intervals]
receive_data = []
threads = []


def parse_line(log_msg):
    p = re.compile(r'\d+')
    num_pair = p.findall(log_msg)
    if len(num_pair) == 2:
        return num_pair
    else:
        return None


def stream_reader(pipe, log_data):
    while True:
        if len(log_data) > 10:
            pipe.kill()
            return
        text = pipe.stdout.readline()
        clock, proc_id = parse_line(str(text))
        log_data.append((int(clock), int(proc_id)))


for i in range(len(pipes)):
    receive_data.append([])
    t = threading.Thread(target=stream_reader, args=(pipes[i], receive_data[i]))
    threads.append(t)
    t.start()

done = [t.join() for t in threads]
table = list(zip(*receive_data))  # transpose list of lists

[print(line) for line in table]   # by device

all_events = []
[all_events.extend(col) for col in receive_data]
all_events = (sorted(all_events, key=lambda x: x[0]))  # all events on the same time axis
[print(line) for line in all_events]   # by device

