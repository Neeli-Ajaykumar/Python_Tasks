#Write a recursive function to calculate the sum of digits of a number. 
def sum(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum(n // 10)
    
print("Sum of a numbers:", sum(1234))
