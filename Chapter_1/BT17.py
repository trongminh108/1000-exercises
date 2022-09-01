"""
Tính S(n) = x + x^2/2! + x^3/3! +...+ x^n/n!
"""

def Fact(n):
    sm = 1
    for i in range(1, n + 1):
        sm *= i
    return sm

x, n = map(int, input("Nhap x, n: ").split())

sm = 0
for i in range(1, n+1):
    sm += pow(x, i)/Fact(i)
    

print("SUM = {}".format(sm))