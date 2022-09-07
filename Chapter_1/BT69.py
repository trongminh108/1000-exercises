"""
69. Tính S(x, n) = x - x^2 +...+ (-1)^n*x^(2n+1)
"""

def BT69_Show(x, n):
    res = 0
    for i in range(n+1):
        res += (-1)**i * x**(2*i+1)
    return res


if __name__ == "__main__":
    while True:
        try:
            x, n = map(int, input("Enter numbers x, n: ").split())
            break
        except:
            print("\nTry Again!")

    print("Result:", BT69_Show(x, n))
