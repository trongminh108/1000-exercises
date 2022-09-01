"""
. Cho hai số nguyên dương a và b. Tìm ước 
chung lớn nhất của hai giá trị này.

"""


def BT62_Show(a, b):
    if b == 0:
        return a
    return BT62_Show(b, a%b)


if __name__ == "__main__":
    while True:
        try:
            a, b = list(map(int, input("Enter the numbers a, b: ").split(", ")))
            break
        except:
            print("\nTry Again!")

    print(f"Greatest common divisor of {a} and {b} is {BT62_Show(a, b)}")