"""
Tính S(n) = 1 + 1/3 + 1/5 +...+1/(2n+1)
"""

n = int(input("Nhap so nguyen n: "))

sum = 0
for i in range(n + 1):
    sum += 1/(2*i+1)

print("Sum = {}".format(sum))