"""
Tính S(n) = 1/2 + 3/4 + 5/6 + (2n+1)/(2n+2)
"""

n = int(input("Nhap so nguyen n: "))

sum = 0
for i in range(n + 1):
    sum += (2*i + 1) / (2*i + 2)

print("Sum = {}".format(sum))