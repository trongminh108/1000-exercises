"""
Tính S(n) = 1 + 1x2 + 1x2x3 +...+ 1x2x3x...xn
"""

n = int(input("Nhap so nguyen n: "))

sum = 0
for i in range(1, n + 1):
    mul = 1
    for j in range(1, i + 1):
        mul *= j
    sum += mul

print("SUM = {}".format(sum))
