"""
Tính S(n) = 1 + x + x^3/3! + x^5/5! +...+ x^(2n+1)/(2n+1)
""" 

def Fact(n):
    sm = 1
    for i in range(1, n + 1):
        sm *= i
    return sm

x, n = map(int, input("Nhap x, n: ").split())

sm = 0
for i in range(n+1):
    sm += pow(x, 2*i+1)/Fact(2*i+1)

print("SUM = {}".format(sm))