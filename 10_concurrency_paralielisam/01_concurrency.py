### Concurrency in Pyhton
print("concurrency in Python")


import threading
import time

def download_file(file_name, duration):
    # print(f"📡 [Thread {threading.current_thread().name}] Starting download: {file_name}...")
    print(f"📡 [Thread {threading.current_thread().name}] Starting download: {file_name}...")
    # print(threading.current_thread())
    
    # time.sleep simulates a network delay (an I/O-bound wait)
    # During this sleep, Python releases the GIL so other threads can run!
    # time.sleep(duration) 
    time.sleep(duration)
    
    print(f"✅ [Thread {threading.current_thread().name}] Finished downloading: {file_name}!")


start_time = time.time()

# thread_1 = threading.Thread(download_file())  ### This is wrong and I made this my mistake

thread_1 = threading.Thread(target=download_file, args=("video", 3), name="A")
thread_2 = threading.Thread(target=download_file, args=("audio" , 2), name="B")
thread_3 = threading.Thread(target=download_file , kwargs={"file_name": "image", "duration": 1 }, name="C")


# Starting all Thread
thread_1.start()
thread_2.start()
thread_3.start()


# Waiting for all thread to complete

thread_1.join()
thread_2.join()
thread_3.join()


print(f"⏱️ Total concurrent execution time: {time.time() - start_time:.2f} seconds")