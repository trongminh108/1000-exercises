"""
Kiểm tra số nguyên 4 byte có dạng 2**k hay không?
"""

from math import log2


def BT75_Show(n):
    num = log2(n)
    return int(num) if num == int(num) else False


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            break
        except:
            print("\nTry Again!")

    res = BT75_Show(n)
    if res:
        print(f"The number {n} if format 2**k with k = {res}")
    else:
        print(f"The number {n} is NOT format 2**k")
