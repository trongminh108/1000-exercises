"""
Đếm số lượng “ước số chẵn” của số nguyên dương n.
"""

from math import sqrt

def SoLuongUocChan(n):
    count = 0
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            if i % 2 == 0:
                count += 1
            j = n // i
            if j != i and j % 2 == 0:
                count += 1
    return count

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    print("So luong uoc chan cua {}: {}".format(n, SoLuongUocChan(n)))

