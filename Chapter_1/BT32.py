"""
Cho số nguyên dương n. Kiểm tra số nguyên dương n có phải là số
chính phương hay không?
"""

from math import sqrt

def Is_PrimeNumber(n):
    if n < 4:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if i**2 == n:
            return True
    return False

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    if Is_PrimeNumber(n):
        print("{} la so chinh phuong".format(n))
    else:
        print("{} khong la so chinh phuong".format(n))


