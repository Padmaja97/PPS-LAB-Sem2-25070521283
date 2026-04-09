num = int(input("Enter a number: "))
temp = abs(num)   # handle negative numbers
digit_sum = 0

while temp > 0:
    digit_sum += temp % 10   # add last digit
    temp //= 10              # remove last digit
print("Sum of digits:", digit_sum)
