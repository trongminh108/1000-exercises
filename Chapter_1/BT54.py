"""
Hãy đếm số lượng chữ số nhỏ nhất của số nguyên dương n.
"""


def BT54_Show(n):
    minn = n % 10
    n //= 10
    count = 1
    while n > 0:
        temp = n % 10
        if minn > temp:
            minn = temp
            count = 1
        elif minn == temp:
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

    print("Result:", BT54_Show(n))