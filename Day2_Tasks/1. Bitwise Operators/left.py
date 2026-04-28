#Write a program to perform left shift (<<) and right shift (>>) operations on a number.
num = int(input("Enter an integer: "))
shift = int(input("Enter number of positions to shift: "))
left_shift = num << shift
right_shift = num >> shift
print(f"\nOriginal number: {num}")
print(f"Number after left shift by {shift} positions: {left_shift}")
print(f"Number after right shift by {shift} positions: {right_shift}")
