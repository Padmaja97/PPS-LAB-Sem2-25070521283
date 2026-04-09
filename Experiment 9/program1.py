# Program to count vowels in a string

text = input()  # Read input string
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(count)

