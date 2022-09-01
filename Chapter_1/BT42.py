"""
Cho n là số nguyên dương. Hãy tìm giá trị nguyên dương k 
lớn nhất sao cho S(k) < n. Trong đó chuỗi S(k) được 
định nghĩa như sau : S(k) = 1 + 2 + 3 + … + k.
"""


def BT42_Show(n):
    k = 0
    sumk = 0
    while sumk < n:
        k += 1
        sumk += k
    k -= 1
    return k


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print("Result:", (BT42_Show(n)))