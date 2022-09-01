"""
Hãy kiểm tra số nguyên dương n có toàn chữ số lẻ hay không?
"""


def BT56_Show(n):
    while n > 0:
        if n % 2 == 0:
            return False
        n //= 10
    return True


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    if BT56_Show(n):
        print(f"The number {n} is full of odd digits")
    else:
        print(f"The number {n} has at least one even digit")