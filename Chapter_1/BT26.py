"""
Tính tích tất cả “ước số lẻ” của số nguyên dương n.

"""

from math import sqrt

def TichUocLe(n):
    mul = 1
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            if i % 2 == 1:
                mul *= i
            j = n // i
            if j != i and j % 2 == 1:
                mul *= j
    return mul

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    print("Tong uoc chan cua {}: {}".format(n, TichUocLe(n)))

