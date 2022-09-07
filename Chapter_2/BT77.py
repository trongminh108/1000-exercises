"""
Kiểm tra số nguyên 4 byte có dạng 3**k hay không?
"""

from math import log


def BT77_Show(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print(f"The sum from 1 to {n} is: {BT77_Show(n)}")
