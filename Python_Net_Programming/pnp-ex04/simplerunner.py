import _thread, time
import random


def handler():
    _id = _thread.get_ident()
    print(f"Hello from thread: {_id}")


for i in range(10):
    id = _thread.start_new_thread(handler, ())
    print(f"Created thread with id: {id}")

time.sleep(random.randint(1, 3))
