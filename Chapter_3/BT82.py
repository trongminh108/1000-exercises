"""
Viết chương trình tìm số lớn nhất trong ba số thực a, b, c
"""
def Show(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c


if __name__ == "__main__":
    while True:
        try:
            a, b, c = map(float, input("Enter numbers a, b, c: ").split())
            break
        except:
            print("\nTry Again!")

    print(f"The biggest number of {a, b, c} is {Show(a, b, c)}")
