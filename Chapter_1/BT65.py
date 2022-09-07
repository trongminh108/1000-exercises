"""
65. Giải phương trình ax^2 + bx + c = 0
"""

from math import sqrt


def BT65_Show(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "has infinitely many solutions"    
            else:
                return "has no solution"
        else:
            return -c/b
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            return " has no solution"
        else:
            x1 = (-b+sqrt(delta))/(2*a)
            x2 = (-b-sqrt(delta))/(2*a)

        if x1 == x2:
            return x1
        return x1, x2


if __name__ == "__main__":
    while True:
        try:
            a, b, c = (map(int, input("Enter your parameters second degree equation: ").split(" ")))
            break
        except:
            print("\nTry Again!")

    res = BT65_Show(a, b, c)
    equation = f"{a}x^2 + {b}x + {c} = 0"
    if type(res) == str:
        print(f"The equation {equation} {res}")
    else:
        print(f"The equation {equation} has solution: {res}")
