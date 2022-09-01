"""
Tính tổng tất cả “ước số chẵn” của số nguyên dương n
"""

from math import sqrt

def TongUocChan(n):
    sum = 0
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
            j = n // i
            if j != i and j % 2 == 0:
                sum += j
    return sum

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    print("Tong uoc chan cua {}: {}".format(n, TongUocChan(n)))

