"""
Tính S(n) = x^n
"""

x, n = map(int, input("Nhap x, n: ").split(", "))

mul = 1
for i in range(n):
    mul *= x

print("Multiply = {}".format(mul))
