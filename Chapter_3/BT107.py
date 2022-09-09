"""
107.Viết hàm tính S = pow(x, 1/n)
(n là số nguyên dương).
"""
def Show(x, n):
    return pow(x, 1/n)
        
if __name__ == "__main__":
    while True:
        try:
            x, n = map(int, input("Enter x and n numbers (n>0): ").split())
            if n < 0:
                raise ValueError
            break
        except:
            print("\nTry Again")

    print("Result:", Show(x, n))
    
    