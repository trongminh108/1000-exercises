"""
Hãy đếm số lượng chữ số của số nguyên dương n
"""

def Show(n):
    return len(str(n))


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print(f"The number of digits of {n} is {Show(n)}")
