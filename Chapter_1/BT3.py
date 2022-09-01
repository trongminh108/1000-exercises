"""
Tính S(n) = 1 + 1/2 + 1/3 +...+1/n
"""

n = int(input("Nhap so nguyen n: "))

sum = 0
for i in range(1, n + 1):
    sum += 1/i

print("Sum =", sum)