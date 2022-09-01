"""
Tính S(n) = 1 + x^2/2! + x^3/3! +...+ x^n/n!
"""

def Fact(n):
    sm = 1
    for i in range(1, n + 1):
        sm *= i
    return sm

x, n = map(int, input("Nhap x, n: ").split())

sm = 0
for i in range(n+1):
    sm += pow(x, 2*i)/Fact(2*i)

print("SUM = {}".format(sm))