"""
Tìm ước số chung lớn nhất của hai số nguyên dương.
"""

def Show(a, b):
    if b == 0:
        return a
    return Show(b, a%b)

if __name__ == "__main__":
    while True:
        try:
            a, b = map(int, input("Enter two positive numbers: ").split())
            if a <= 0 or b <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again")

    print(f"The Greatest common divisor of {a} and {b} is: {Show(a, b)}")    