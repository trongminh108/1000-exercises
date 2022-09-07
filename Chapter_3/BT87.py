"""
Tìm số nguyên dương n nhỏ nhất sao cho 1 + 2 + … + n > 10000.
"""

def Show(n=10000):
    res = 0
    k = 1
    while res <= n:
        res += k
        k += 1
    return k-1

if __name__ == "__main__":
    print("Result:", Show(100))
    
    