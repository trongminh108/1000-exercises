"""
Hãy tìm chữ số đảo ngược của số nguyên dương n.
"""


def BT50_Show(n):
    res = 0
    while n > 0:
        res = res*10 + n%10
        n //= 10
    return res

def ReverseNumber(n):
    res = ""
    while n > 0:
        res += str(n%10)
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

    print("Result:", BT50_Show(n))
    print("Result:", ReverseNumber(n))