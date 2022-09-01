"""
Tính S(n) = 1 x 2 x 3 x...x n
"""

n = int(input("Nhap so nguyen n: "))

mul = 1
for i in range(1, n + 1):
    mul *= i

print("Multiply = {}".format(mul))