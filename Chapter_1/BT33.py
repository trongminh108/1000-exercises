"""
Tính S(n) = sqrt(2+sqrt(2+...sqrt(2))) có n dấu căn
"""

from math import sqrt

def CanN(n):
    sum = 0
    for i in range(n):
        sum = sqrt(2 + sum)
    return sum

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    print("Can n: {}".format(CanN(n)))


