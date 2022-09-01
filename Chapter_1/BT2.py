"""
Tính S(n) = 1^2 + 2^2 + 3^2 + … + n^2
"""

n = int(input("Nhap so nguyen n: "))

sum = 0
for i in range(1, n + 1):
    sum += i**2

print("Sum =", sum)