"""
Liệt kê tất cả “ước số lẻ” của số nguyên dương n
"""

from math import sqrt

def DemSoLuongUocLe(n):
    lst = []
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            if i % 2 == 1:
                lst.append(i)
            j = n // i
            if j != i and j % 2 == 1:
                lst.append(j)
    lst.sort()
    lst = [str(i) for i in lst]
    return " ".join(lst)

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    print("So luong cac uoc le cua {}: {}".format(n, DemSoLuongUocLe(n)))

