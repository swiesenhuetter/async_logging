import threading
import time
import sys
import os
import signal

"""
periodically do some work (print time and process id) 
until stop_event occurs
"""

if __name__ == "__main__":
    t0 = int(1000.0 * time.time())
    """ process start time in ms"""

    if len(sys.argv) > 1:
        interval = float(sys.argv[-1])
    else:
        print('interval missing')
        exit(-1)

    stop_evt = threading.Event()

    def shut_down(signal_received, frame):
        stop_evt.set()
    signal.signal(signal.SIGINT, shut_down)
    if os.name == 'nt':
        signal.signal(signal.SIGBREAK, shut_down)
    else :
        signal.signal(signal.SIGTERM, shut_down)


    while True:
        t_now = int(1000.0*time.time()) - t0
        msg = 'Clock {} from {}'.format(t_now, os.getpid())
        print(msg, flush=True)
        stop_evt.wait(interval)
        if stop_evt.is_set():
            break

