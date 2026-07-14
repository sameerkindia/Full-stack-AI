from multiprocessing import Process
import threading
import time


def heavy_cpu_work():
    # count = 0
    for _ in range(100_000_000):
        # count += 1
        pass


### With thread

# start_time = time.time()

# t1 = threading.Thread(target=heavy_cpu_work)
# t2 = threading.Thread(target=heavy_cpu_work)

# t1.start()
# t2.start()

# t1.join()
# t2.join()


# print(f"Thread work end at {time.time() - start_time}")




### With process


if __name__ == "__main__":
    start_time = time.time()

    processes = [Process(target=heavy_cpu_work) for _ in range(0, 2)]

    [p.start() for p in processes]
    [p.join for p in processes]

    print(f"Process work end at {time.time() - start_time}")
