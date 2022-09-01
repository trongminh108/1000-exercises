"""
Cho số nguyên dương n. Kiểm tra số dương n có phải là số hoàn thiện
hay không?
"""

from math import sqrt

def Is_PerfectNumber(n):
    sum = 1
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            sum += i
            j = n // i
            if j != i:
                sum += j
    return sum == n

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    if Is_PerfectNumber(n):
        print("{} la so hoan hao".format(n))
    else:
        print("{} khong la so hoan hao".format(n))


