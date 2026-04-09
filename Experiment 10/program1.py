# Program to remove punctuation marks from a string

text = input()  # Read input string

# Keep only alphanumeric characters and spaces
result = "".join(char for char in text if char.isalnum() or char == " ")

print(result)
