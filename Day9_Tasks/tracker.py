"""Performance Tracker (Decorators) 
A software team wants to track how long functions take to execute. Create a decorator 
that measures and prints the execution time of a function."""

import time
def time_tracker(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Start time:", start)
        print("End time:", end)
        print("Execution time:", end - start, "seconds")
    return wrapper

@time_tracker
def task():
    print("Task is running...")
    time.sleep(5)

task()
