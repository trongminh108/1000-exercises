"""
Tính S(n) = sqrt(n!+sqrt((n-1)!+...sqrt(1!))) có n dấu căn
"""

from math import sqrt

def Fact(n):
    mul = 1
    for i in range(2, n+1):
        mul *= i
    return mul

def CanN3(n):
    sum = 0
    for i in range(1, n+1):
        sum = sqrt(Fact(i) + sum)
    return sum

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    print("Can n: {}".format(CanN3(n)))


