# Program to check if a string is a palindrome

text = input()  # Read input string

# Reverse the string and compare with the original
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
