"""
Tính S(n) = x + x^2/(1+2) + x^3/(1+2+3) +...+ x^n/(1+2+3+...+n)
"""

def Sum(n):
    lst = [i for i in range(n+1)]
    return sum(lst)

x, n = map(int, input("Nhap x, n: ").split())

s = 0
for i in range(1, n+1):
    s += pow(x, i)/Sum(i)

print("Sum = {}".format(s))