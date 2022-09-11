"""
117. Viết chương trình nhập n và tính tổng
S(x, n) = x + x^2 + x^3 + ... + x^n
"""

def Show(x=0, n=1):
    return sum([x**i for i in range(1, n+1)])
        
def another_Show(x=0, n=1):
    res = x
    for i in range(2, n+1):
        res += x**i
    return res

if __name__ == "__main__":
    while True:
        try:
            x, n = map(int, input("Enter positive numbers x and n: ").split())
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again")

    print("Result:", Show(x, n))
    print("Result:", another_Show(x, n))

    