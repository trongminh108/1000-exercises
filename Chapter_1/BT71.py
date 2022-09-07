"""
71. Tính S(x, n) = -x + x^2/(1+2) - x^3/(1+2+3) +...+ (-1)^n*x^n/(1+2+...+n)
"""
def sum(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

def BT70_Show(x, n):
    res = 0
    for i in range(1, n+1):
        res += (-1)**(i) * x**i / sum(i)
    return res


if __name__ == "__main__":
    while True:
        try:
            x, n = map(int, input("Enter numbers x, n: ").split())
            break
        except:
            print("\nTry Again!")

    print("Result:", BT70_Show(x, n))
