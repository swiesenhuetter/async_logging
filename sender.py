import threading
import time
import sys
import os
import signal

t0 = int(1000.0 * time.time())  # process start time in ms

if len(sys.argv) > 1:
    interval = float(sys.argv[1])
else:
    print('interval missing')
    exit(-1)

stop_evt = threading.Event()
if sys.platform == 'win32':
    signal.signal(signal.SIGBREAK, lambda: stop_evt.set())

while True:
    """
    periodically do some work (print time and process id) 
    """
    t_now = int(1000.0*time.time()) - t0
    msg = 'Clock {} from {}'.format(t_now, os.getpid())
    print(msg, flush=True)
    stop_evt.wait(interval)
    if stop_evt.is_set():
        break

