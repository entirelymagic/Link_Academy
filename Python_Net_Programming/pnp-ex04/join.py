import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(1, 11):
            print(i)
            time.sleep(0.5)


mt1 = MyThread()
mt2 = MyThread()

mt1.start()
mt2.start()

mt1.join(2)  # can take a parameter the number of seconds to wait the thread before moving on.
print("This happened.")
