"""
Tính S(x, n) = x + x^2/(1+2) +...+ x^n/(1+2+3+...+n)
"""



def s(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

def Show(x, n):
    res = 0
    for i in range(1, n+1):
        res += x**i / s(i)
    return res


if __name__ == "__main__":
    while True:
        try:
            x, n = map(int, input("Enter positive number n: ").split())
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print(f"S({n}) = {Show(x, n)}")
