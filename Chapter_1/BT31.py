"""
Cho số nguyên dương n. Kiểm tra số nguyên dương n có phải là số
nguyên tố hay không?
"""

from math import sqrt

def Is_PrimeNumber(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    if Is_PrimeNumber(n):
        print("{} la so nguyen to".format(n))
    else:
        print("{} khong la so nguyen to".format(n))


