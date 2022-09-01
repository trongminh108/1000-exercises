"""
Hãy đếm số lượng chữ số lớn nhất của số nguyên dương n.
"""


def BT53_Show(n):
    maxn = n % 10
    n //= 10
    count = 1
    while n > 0:
        temp = n % 10
        if maxn < temp:
            maxn = temp
            count = 1
        elif maxn == temp:
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

    print("Result:", BT53_Show(n))