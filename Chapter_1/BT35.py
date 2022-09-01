"""
Tính S(n) = sqrt(1+sqrt(2+...sqrt(n-1+sqrt(1)))) có n dấu căn
"""

from math import sqrt

def CanN2(n):
    sum = 0
    for i in range(n, 0, -1):
        sum = sqrt(i + sum)
    return sum

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    print("Can n: {}".format(CanN2(n)))


