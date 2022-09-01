"""
Hãy đếm số lượng chữ số của số nguyên dương n
"""


def BT43_Show(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print("Result:", (BT43_Show(n)))