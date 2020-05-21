import threading
from threading import current_thread
import time


def MyThread(name, old):
    print(current_thread().getName(), "start")
    print(name, old)
    time.sleep(1)
    print(current_thread().getName(), "end")


for i in range(1, 6, 1):
    t1 = threading.Thread(target=MyThread, args=("hore", i))
    t1.start()

for i in range(1, 6, 1):
    t2 = threading.Thread(target=MyThread, args=("t2", i))
    t2.join()

t2.run()
