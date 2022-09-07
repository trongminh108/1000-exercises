"""
Viết chương trình tính tổng các giá trị lẻ nguyên dương nhỏ hơn N.
"""

def Show(n):
    res = 0
    for i in range(1, n, 2):
        res += i
    return res

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again")
    print(f"The sum of odd numbers from 1 to {n}: {Show(n)}")
    