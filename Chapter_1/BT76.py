"""
Kiểm tra số nguyên 4 byte có dạng 3**k hay không?
"""

from math import log


def BT76_Show(n):
    num = log(n, 3)
    return int(num) if num == int(num) else False


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            break
        except:
            print("\nTry Again!")

    res = BT76_Show(n)
    if res:
        print(f"The number {n} if format 3**k with k = {res}")
    else:
        print(f"The number {n} is NOT format 3**k")
