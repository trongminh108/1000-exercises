"""
Tính tích tất cả “ước số” của số nguyên dương n.
"""

from math import sqrt

def TichUoc(n):
    mul = 1
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            mul *= i
            j = n // i
            if j != i:
                mul *= j
    return mul

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    print("Tich cac uoc cua {}: {}".format(n, TichUoc(n)))

