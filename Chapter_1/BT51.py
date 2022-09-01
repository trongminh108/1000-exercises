"""
Tìm chữ số lớn nhất của số nguyên dương n.
"""


def BT51_Show(n):
    maxn = n % 10
    n //= 10
    while n > 0:
        temp = n % 10
        maxn = maxn if maxn > temp else temp
        n //= 10
    return maxn


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print("Result:", BT51_Show(n))