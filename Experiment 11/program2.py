def sum_of_digits_recursive(n):
	if n == 0:
		return 0
	return (n % 10) + sum_of_digits_recursive( n // 10  )
number = input()
if number.strip():
	number = int(number)
result = sum_of_digits_recursive(number)	
print(result)
