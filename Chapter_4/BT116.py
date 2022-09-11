"""
116.Viết chương trình nhập n và tính tổng
S(n) = 1 + 2 + 3 + … + n.
"""

def Show(n=0):
    return sum([i for i in range(1, n+1)])
        
def another_Show(n=0):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter a positive number: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again")

    print("The sum from 1 to n is:", Show(n))
    print("The sum from 1 to n is:", another_Show(n))

    