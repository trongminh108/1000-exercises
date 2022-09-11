"""
119.Liệt kê tất cả các số nguyên tố nhỏ hơn n.
"""

from math import sqrt


def Show(n):
    sieve = [True] * (n+1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(sqrt(n)+1)):
        if sieve[i] == True:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    
    res = []
    for idx, val in enumerate(sieve):
        if val:
            res.append(str(idx))

    return ", ".join(res)

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter a positive number: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again")

    print("The prime numbers less than n:", Show(n))

    