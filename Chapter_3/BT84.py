"""
Giải phương trình và biện luận phương trình ax + b = 0.
"""
def Show(a, b):
    return -b/a


if __name__ == "__main__":
    while True:
        try:
            a, b = map(float, input("Enter numbers a, b (a != 0): ").split())
            if a == 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print(f"The solution of equation {a}x + {b} = 0 is {Show(a, b)}")