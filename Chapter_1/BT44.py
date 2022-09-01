"""
Hãy tính tổng các chữ số của số nguyên dương n.
"""


def BT44_Show(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
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

    print("Result:", (BT44_Show(n)))