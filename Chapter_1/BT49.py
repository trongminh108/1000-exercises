"""
Cho số nguyên dương n. Hãy tìm chữ số đầu tiên của n.
"""


def BT49_Show(n):
    while n > 10:
        n //= 10
    return n


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print("Result:", (BT49_Show(n)))