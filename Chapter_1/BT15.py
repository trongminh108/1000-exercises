"""
Tính S(n) = 1 + 1/(1+2) + 1/(1+2+3) + 1/(1+2+3+...+n)
"""

def Sum(n):
    lst = [i for i in range(n+1)]
    return sum(lst)

n = int(input("Nhap so nguyen n: "))

s = 0
for i in range(1, n+1):
    s += 1/Sum(i)

print("Sum = {}".format(s))