"""
Hãy đếm số lượng chữ số lẻ của số nguyên dương n
"""


def BT46_Show(n):
    count = 0
    while n > 0:
        if n % 2:
            count += 1
        n //= 10
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

    print("Result:", (BT46_Show(n)))