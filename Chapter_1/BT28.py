"""
Cho số nguyên dương n. Tính tổng các ước số nhỏ hơn chính nó
"""

from math import sqrt

def TongUoc(n):
    res = 0
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            j = n // i
            res += i + j
    return res

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    print("Tong uoc nho hon {}: {}".format(n, TongUoc(n)))

