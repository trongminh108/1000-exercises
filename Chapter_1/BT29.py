"""
Tìm ước số lẻ lớn nhất của số nguyên dương n. Ví dụ n = 100 ước lẻ
lớn nhất của 100 là 25.
"""

from math import sqrt

def UocLeLonNhat(n):
    if n % 2 == 1:
        return n
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            j = n // i
            if j % 2 == 1:
                return j
    return 1

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    print("Uoc le lon nhat cua {}: {}".format(n, UocLeLonNhat(n)))

