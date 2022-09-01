"""
Tính tổng tất cả “ước số” của số nguyên dương n.
"""

from math import sqrt

def TongUoc(n):
    sum = 0
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            sum += i
            if n // i != i:
                sum += n // i
    return sum

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    print("Tong cac uoc cua {}: {}".format(n, TongUoc(n)))

