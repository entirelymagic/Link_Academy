import threading
import time


class MyThread(threading.Thread):
    """A Thread with a correct stopping behavior."""
    # flag to stop the thread.
    active = False

    def stop_thread(self):
        self.active = False

    def run(self):
        self.active = True
        print("I am going to sleep 10 seconds")
        for i in range(10000):
            t = time.perf_counter()
            # time.sleep(0.1)
            t = time.perf_counter() - t
            print(f"Thread is running id={i} time {t}")
            if not self.active:
                return
            # print(f"Thread is running, ran {i} times.")
        print('Thread completed!')


mt = MyThread()  # initialize the thread.
mt.start()  # start the second thread
time.sleep(10)  # sleep on main thread.
print("Hey, wake up!")
mt.stop_thread()  # stop the second thread

# main thread will stop.
