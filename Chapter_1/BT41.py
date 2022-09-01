"""
Tính S(n) = 1 + 1/(1 + 1/(1+1)) có n dấu phân số
"""


def BT41_Show(n):
    res = 1
    for i in range(1, n+1):
        res = 1/(1+res)
    return res


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print("Result:", round(BT41_Show(n), 9))