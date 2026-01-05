import threading
import time

def worker(num):
    print(f"Thread {num}: Starting")
    time.sleep(2) # Simulate some work
    print(f"Thread {num}: Finishing")