"""
Tính S(n) = x^2 + x^4 +...+ x^2n
"""

x, n = map(int, input("Nhap x, n: ").split())

sum = 0
for i in range(1, n + 1):
    sum += pow(x, i*2)

print("SUM = {}".format(sum))
