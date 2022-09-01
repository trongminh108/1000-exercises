"""
Tính S(n) = x + x^3 + x^5 +...+ x^(2n+1)
"""

x, n = map(int, input("Nhap x, n: ").split())

sum = 0
for i in range(n + 1):
    sum += pow(x, i*2+1)

print("SUM = {}".format(sum))
