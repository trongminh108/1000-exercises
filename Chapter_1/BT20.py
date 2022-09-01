"""
Liệt kê tất cả "ước số" của số nguyên dương n.
"""

from math import sqrt

def LietKeUoc(n):
    lst = []
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            lst.append(i)
            if n//i not in lst:
                lst.append(n//i)
    lst.sort()
    lst = [str(i) for i in lst]
    print(f"Uoc cua {n}: "+ ", ".join(lst))

if __name__ == "__main__":

    n = int(input("Nhap so nguyen duong n: "))
    LietKeUoc(n)

