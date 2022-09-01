"""
Đếm số lượng “ước số” của số nguyên dương n.

"""

from math import sqrt

def DemSoLuongUoc(n):
    count = 0
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            count += 1
            j = n // i
            if j != i:
                count += 1
    return count

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    print("So luong cac uoc cua {}: {}".format(n, DemSoLuongUoc(n)))

