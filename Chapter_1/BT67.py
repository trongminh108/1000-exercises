"""
67. Tính S(x, n) = x - x^2 +...+ (-1)^(n+1)*x^n
"""

def BT67_Show(x, n):
    res = 0
    for i in range(n+1):
        res += (-1)**(i+1) * x**i
    return res


if __name__ == "__main__":
    while True:
        try:
            x, n = (map(int, input("Enter numbers x, n: ").split()))
            break
        except:
            print("\nTry Again!")

    print("Result:", BT67_Show(x, n))
