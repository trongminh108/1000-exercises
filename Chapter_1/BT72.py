"""
72. Tính S(x, n) = -x + x^2/2! - x^3/3! +...+ (-1)^n*x^n/n!
"""
def f(n):
    if n <= 1:
        return 1
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def BT72_Show(x, n):
    res = 0
    for i in range(1, n+1):
        res += (-1)**i * x**i / f(i)
    return res


if __name__ == "__main__":
    while True:
        try:
            x, n = map(int, input("Enter numbers x, n: ").split())
            break
        except:
            print("\nTry Again!")

    print("Result:", BT72_Show(x, n))
