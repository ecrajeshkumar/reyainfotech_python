import threading
import time

def worker(name):
    print(f"Thread {name} starting")
    time.sleep(2)
    print(f"Thread {name} finishing")

# create threads
thread1 = threading.Thread(target=worker, args=("A",))
thread2 = threading.Thread(target=worker, args=("B",))

# start threads
thread1.start()
thread2.start()

# wait for threads to complete
thread1.join()
thread2.join()

