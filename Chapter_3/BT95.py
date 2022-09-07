"""
Viết chương trình nhập 3 số thực. Hãy thay tất cả các số 
âm bằng trị tuyệt đối của nó.
"""


def Show(a, b, c):
    return abs(a), abs(b), abs(c)

if __name__ == "__main__":
    while True:
        try:
            a, b, c = map(float, input("Enter three numbers: ").split())
            break
        except:
            print("\nTry Again")

    print("Result:", Show(a, b, c))
        