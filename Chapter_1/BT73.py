"""
Tính S(x, n) = -1 + x^2/2! - x^4/4! +...+ (-1)**(n+1) * x^(2n) / (2n)!
"""
def f(n):
    if n <= 1:
        return 1
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def BT73_Show(x, n):
    res = 0
    for i in range(1, n+1):
        res += (-1)**(i+1) * x**(2*i) / f(2*i)
    return res


if __name__ == "__main__":
    while True:
        try:
            x, n = map(int, input("Enter numbers x, n: ").split())
            break
        except:
            print("\nTry Again!")

    print("Result:", BT73_Show(x, n))
