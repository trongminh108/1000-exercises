"""
120.Liệt kê tất cả các số chính phương nhỏ hơn n.
"""

from math import sqrt

def Show(n):
    return ", ".join([str(i*i) for i in range(1, int(sqrt(n)+1))])

def another_Show(n):
    res = []
    for i in range(1, int(sqrt(n)+1)):
        res.append(str(i*i))
    
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

    print("The square numbers less than n:", Show(n))
    print("The square numbers less than n:", another_Show(n))

    