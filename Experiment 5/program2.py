# Read marks of four subjects
m1, m2, m3, m4 = map(int, input().split())

# Calculate total
total = m1 + m2 + m3 + m4

# Calculate aggregate percentage
aggregate = total / 4

# Determine grade
if aggregate > 75:
    grade = "Distinction"
elif aggregate >= 60 and aggregate < 75:
    grade = "First Division"
elif aggregate >= 50 and aggregate < 60:
    grade = "Second Division"
elif aggregate >= 40 and aggregate < 50:
    grade = "Third Division"
else:
    grade = "Fail"

# Output
print(total)
print(f"{aggregate:.2f}")
print(grade)
