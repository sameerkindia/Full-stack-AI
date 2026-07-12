import threading
import time


COUNTDOWNN_LIMIT = 30_000_000

def cpu_heavy_task():
    n = COUNTDOWNN_LIMIT

    while n > 0:
        n -= 1




### Sequential Execution (One after another)

print("⏳ Running sequentially on a single thread...")

start_time = time.time()

cpu_heavy_task()
cpu_heavy_task()
# heavy_task_1 = threading.Thread(target=cpu_heavy_task)

# heavy_task_1.start()
# heavy_task_1.join()

sequential_duration = time.time() - start_time
print(f"✅ Sequential Total Time: {sequential_duration:.2f} seconds\n")





### Multithreaded Execution 

print("📡 Running concurrently with two OS threads...")
start_time = time.time()

thread1 = threading.Thread(target=cpu_heavy_task)
thread2 = threading.Thread(target=cpu_heavy_task)

thread1.start()
thread2.start()

print("Just for testing")

thread1.join()

print("Just for testing 2")

thread2.join()

threaded_duration = time.time() - start_time
print(f"✅ Multithreaded Total Time: {threaded_duration:.2f} seconds\n")



def fetch_data(api_url):
    print(f"Starting request for {api_url}")
    time.sleep(2)  # Simulates network wait (Drops the GIL automatically)
    print(f"Finished fetching {api_url}")

# Spin up parallel network workers
t1 = threading.Thread(target=fetch_data, args=("api/users",))
t2 = threading.Thread(target=fetch_data, args=("api/products",))

t1.start()
t2.start()
t1.join()  # Wait for workers to finish
t2.join()