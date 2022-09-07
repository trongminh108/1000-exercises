"""
66. Giải phương trình ax^4 + bx^2 + c = 0
"""

from math import sqrt


def BT66_Show(a, b, c):
    res = []
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
            x1 = (-b-sqrt(delta))/(2*a)
            x2 = (-b+sqrt(delta))/(2*a)
            if x1 >= 0:
                x1 = str(sqrt(x1))
                res.append(x1)
                res.append("-"+x1)
            else:
                x1 = str(sqrt(-x1))
                res.append(x1+"i")
                res.append("-"+x1+"i")
            if x2 >= 0:
                x2 = str(sqrt(x2))
                res.append(x2)
                res.append("-"+x2)
            else:
                x2 = str(sqrt(-x2))
                res.append(x2+"i")
                res.append("-"+x2+"i")
        try:
            if res[0] == res[2]:
                return res[:2]
        except:
            return res
        return res


if __name__ == "__main__":
    while True:
        try:
            a, b, c = (map(int, input("Enter your parameters second degree equation: ").split(" ")))
            break
        except:
            print("\nTry Again!")

    res = BT66_Show(a, b, c)
    equation = f"{a}x^4 + {b}x^2 + {c} = 0"
    if type(res) == str:
        print(f"The equation {equation} {res}")
    else:
        res = ", ".join(res)
        print(f"The equation {equation} has solution: {res}")
