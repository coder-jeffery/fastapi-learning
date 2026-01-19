from concurrent.futures import thread
from datetime import time


class threadlearning:

    def print_time(self, threadName, delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print ( threadName, time.ctime(time.time()))

    try:
        thread.start_new_thread(print_time, ("Thread-1", 2,))
        thread.start_new_thread(print_time, ("Thread-2", 4,))
    except:
        print("Error: unable to start thread")

    while 1:
        pass

# threadTools = threadlearning()
# threadTools.print_time("Thread-1", 2)
# print(threadTools.print_time("Thread-2", 3))
