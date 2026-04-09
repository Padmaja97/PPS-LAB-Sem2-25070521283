n = input()
if n.strip():
	n=int(n)
	for i in range(n, 0, -1):
		print('*' * i)
