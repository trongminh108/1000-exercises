"""
Tính S(n) = x^1 + x^2 +...+ x^n
"""

x, n = map(int, input("Nhap x, n: ").split())

sum = 0
for i in range(1, n + 1):
    sum += pow(x, i)

print("SUM = {}".format(sum))
