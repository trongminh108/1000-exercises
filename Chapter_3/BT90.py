"""
Viết chương trình tìm số nguyên dương m lớn nhất sao cho
1 + 2 + 3 + … + m < N. Với N được nhập từ bàn phím
"""


def Show(n):
    m = 0
    res = 0
    while res < n:
        m += 1
        res += m
    return m-1

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again")
    print("Result:", Show(n))
    