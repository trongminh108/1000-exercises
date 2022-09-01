"""
Tính S(n) = pow(n + pow(n-1 +...+sqrt(2), 1/(n-1)), 1/n) có n - 1 dấu căn
"""

from math import sqrt


def BT37_Show(n):
    res = pow(2, 1/2)

    for i in range(3, n+1):
        res = pow(i + res, 1/i)

    return res


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the positive number: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print("Result:", BT37_Show(n))