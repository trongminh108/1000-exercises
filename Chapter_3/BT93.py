"""
Viết chương trình kiểm tra một số có phải số nguyên tố 
hay không.
"""

from math import sqrt


def Show(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter a number: "))
            break
        except:
            print("\nTry Again")

    if Show(n):
        print(f"The number {n} is prime number")
    else:
        print(f"The number {n} is NOT prime number")
        