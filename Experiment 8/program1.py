n = int(input("dimension: "))
print("first matrix:")
matrix1 = []
for _ in range(n):
	matrix1.append(list(map(int, input().split())))
print("second matrix:")
matrix2 = []
for _ in range(n):
	matrix2.append(list(map(int, input().split())))
result = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
	for j in range(n):
		for k in range(n):
			result[i][j] += matrix1[i][k] * matrix2[k][j]
print("Resultant Matrix:")
for row in result:
	print(*(row))
