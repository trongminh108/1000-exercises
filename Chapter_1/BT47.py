"""
Hãy tính tổng các chữ số chẵn của số nguyên dương n.
"""


def BT47_Show(n):
    res = 0
    while n > 0:
        temp = n % 10
        if temp % 2 == 0:
            res += temp
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

    print("Result:", (BT47_Show(n)))