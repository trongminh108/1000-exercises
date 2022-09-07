"""
Viết chương trình nhập vào hai số thực. Kiểm tra xem chúng có cùng
dấu hay không.
"""
def Show(a, b):
    if a * b > 0:
        return True
    return False


if __name__ == "__main__":
    while True:
        try:
            a, b = map(float, input("Enter numbers a, b (diff 0): ").split())
            if a == 0 or b == 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    if Show(a, b):
        print(f"{a} and {b} has the same sign")
    else:
        print(f"{a} and {b} has NOT the same sign")