import threading
import time


count = 0
lock = threading.Lock()


def inc_count():
    global count

    for cur in range(0,10):
        time.sleep(0.2)
        # with lock:
        count += 1
        print(f"{threading.current_thread().name}'s count is {count} at {cur + 1}")
    
    # print(f"{threading.current_thread().name}'s count is {count}")

def dec_count():
    global count

    for cur in range(0,10):
        time.sleep(0.2)
        # with lock:
        count -= 1
        print(f"{threading.current_thread().name}'s count is {count} at {cur + 1}")
    
    # print(f"{threading.current_thread().name}'s count is {count}")


start_time = time.time()

t1 = threading.Thread(target=inc_count, name="Car")
t2 = threading.Thread(target=dec_count, name="Bike...................")

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Threads End time {time.time() - start_time}")