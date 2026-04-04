#Write a recursive function to find the nth Fibonacci number. 
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
for i in range(10):
    print(fibonacci(i))
