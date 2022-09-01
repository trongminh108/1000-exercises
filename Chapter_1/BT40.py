"""
Tính S(n) = sqrt(x^n + sqrt(x^(n-1) +...+ sqrt(x))) có n dấu căn
"""

from math import sqrt

def BT40_Show(x, n):
    res = sqrt(x)

    for i in range(2, n+1):
        res = sqrt(x**i + res)

    return res


if __name__ == "__main__":
    while True:
        try:
            x, n = list(map(int, input("Enter positive numbers x, n: ").split(", ")))
            if n <= 0 or x <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")
            print("Input format x, n (ex: 3, 4)")

    print("Result:", round(BT40_Show(x, n), 9))