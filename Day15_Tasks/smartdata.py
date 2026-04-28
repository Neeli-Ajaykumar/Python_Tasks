"""Smart Data Processing Pipeline 
Scenario: 
A system processes numeric data from file. 
Task: 
● Read numbers from a file 
● Use NumPy for calculations (mean, std) 
● Convert results to Pandas DataFrame 
● Use exception handling for bad data 
● Use a generator to stream data 
● Apply decorator to measure execution time """

import numpy as np
import pandas as pd
import time

def timer(func):
    def wrapper():
        start = time.time()
        print("Start:", start)
        
        end = time.time()
        print("\nEnd:", end)
        
        func()
        print("\nExecution Time:", end - start)
    return wrapper

def read_numbers(file):
    for line in open(file):
        try:
            yield float(line)
        except:
            print("Bad data skipped")

@timer
def process():
    nums = []
    for n in read_numbers("numbers.txt"):
        nums.append(n)
    arr = np.array(nums)
    df = pd.DataFrame({"Mean": [np.mean(arr)], "Std": [np.std(arr)]})
    print(df)
process()
