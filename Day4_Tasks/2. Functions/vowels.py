#Write a function that takes a string as input and returns the number of vowels.
def vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in text:
        if ch in vowels:
            count = count + 1
    return count
str = "helloo"
result = vowels(str)
print(result)
