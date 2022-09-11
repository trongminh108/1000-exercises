"""
120.Liệt kê tất cả các số chính phương nhỏ hơn n.
"""

from math import sqrt

def Show(n):
    str_n = str(n)
    res = 0

    for num in str_n:
        res += int(num)**len(str_n)

    return res == n



if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter a positive number: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again")

    res = []
    for i in range(1, n+1):
        if Show(i):
            res.append(str(i))

    print("The armstrong numbers from 1 to n: " + ", ".join(res))

    