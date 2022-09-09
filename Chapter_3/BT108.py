"""
108.Viết hàm tính S = x^y
"""
def Show(x, y):
    return pow(x, y)
        
if __name__ == "__main__":
    while True:
        try:
            x, y = map(int, input("Enter x and n numbers (n>0): ").split())
            if x == 0 and y <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again")

    print("Result:", Show(x, y))
    
    