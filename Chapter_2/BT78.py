"""
Liệt kê tất cả các ước số của số nguyên dương n.
"""

from math import sqrt


def Show(n):
    res = []
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            res.append(i)
            j = n//i
            if j != i:
                res.append(j)
    res.sort()
    res = [str(i) for i in res]
    return ", ".join(res)


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print(f"The divisor of {n} is {Show(n)}")
