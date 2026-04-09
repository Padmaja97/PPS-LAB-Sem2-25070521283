import math
start = int(input())
end = int(input())
prime_found = []
for num in range(start, end + 1):
	if num > 1:
		is_prime = True
		for i  in range(2, int(math.sqrt(num)) + 1):
			if num % i == 0:
				is_prime = False
				break
		if is_prime:
			prime_found.append(num)
if not prime_found:
	print("No primes")
else:
	for prime in prime_found:
		print(prime)
