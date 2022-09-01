"""
Tính S(n) = 1/2 + 2/3 + 3/4 +...+ n/(n+1)
"""

n = int(input("Nhap so nguyen n: "))

sum = 0
for i in range(1, n + 1):
    sum += i / (i+1)

print("Sum = {}".format(sum))