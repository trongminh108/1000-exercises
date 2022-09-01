"""
Tính S(n) = 1/(1x2) + 1/(2x3) +...+1/(n(n+1))
"""

n = int(input("Nhap so nguyen n: "))

sum = 0
for i in range(1, n + 1):
    sum += 1/(i * (i + 1))

print("Sum = {}".format(sum))