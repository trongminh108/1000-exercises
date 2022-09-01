"""
Cho hai số nguyên dương a và b. Tìm bội chung nhỏ nhất
của hai giá trị này.

"""


def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)

def BT63_Show(a, b):
    return (a*b)//GCD(a, b)


if __name__ == "__main__":
    while True:
        try:
            a, b = list(map(int, input("Enter the numbers a, b: ").split(", ")))
            break
        except:
            print("\nTry Again!")

    print(f"Least common multiple of {a} and {b} is {BT63_Show(a, b)}")