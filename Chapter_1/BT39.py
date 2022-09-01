"""
Tính S(n) = pow(n! + pow((n-1)!+...sqrt(1!), 1/(n+1)), 1/n) có n dấu căn
"""

from math import sqrt

def f(n):
    if n <= 1:
        return 1
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def BT39_Show(n):
    res = 1

    for i in range(2, n+1):
        res = pow(f(i) + res, 1/(i+1))

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

    print("Result:", round(BT39_Show(n), 9))