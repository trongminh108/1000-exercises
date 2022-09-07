"""
In tất cả các số nguyên dương lẻ nhỏ hơn 100.
"""

def Show(n=100):
    res = []
    for i in range(1, n+1, 2):
        res.append(str(i))
    return ", ".join(res)

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again")
    print(f"The odd numbers less than {n}: {Show(n)}")
    