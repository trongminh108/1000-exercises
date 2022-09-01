"""
Tính S(n) = 1/2 + 1/4 +...+1/2n
"""

n = int(input("Nhap so nguyen n: "))

sum = 0
for i in range(1, n + 1):
    sum += 1/(2*i)

print("Sum = {}".format(sum))