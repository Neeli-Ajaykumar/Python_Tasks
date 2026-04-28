"""Infinite Even Number Generator (Generators) 
Create a generator function that continuously generates even numbers starting from 
2. The program should print the first N even numbers using this generator. """

def even_numbers():
    num = 2
    while True:
        yield num
        num = num + 2

N = int(input("Enter how many even numbers to print: "))
gen = even_numbers()
for i in range(N):
    print(next(gen))
