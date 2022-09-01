"""
Hãy tính tích các chữ số lẻ của số nguyên dương n.
"""


def BT48_Show(n):
    res = 1
    while n > 0:
        temp = n % 10
        if temp % 2:
            res *= temp
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

    print("Result:", (BT48_Show(n)))