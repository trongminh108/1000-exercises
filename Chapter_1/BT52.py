"""
Tìm chữ số nhỏ nhất của số nguyên dương n.
"""


def BT52_Show(n):
    minn = n % 10
    n //= 10
    while n > 0:
        temp = n % 10
        minn = minn if minn < temp else temp
        n //= 10
    return minn


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print("Result:", BT52_Show(n))