import threading
import time
import sys
import os


t0 = int(1000.0 * time.time())  # process start time in ms

if len(sys.argv) > 1:
    interval = float(sys.argv[1])
else:
    print('interval missing')
    exit(-1)


ev = threading.Event()


def timer_elapsed():
    t_now = int(1000.0*time.time()) - t0
    msg = 'Clock {} from {}'.format(t_now, os.getpid())
    print(msg)
    ev.set()


while True:
    threading.Timer(interval, timer_elapsed).start()
    ev.wait()
    if ev.is_set():
        ev.clear()
    else:
        print('.')


