"""
109.Viết chương trình in bảng cửu chương ra màn hình.
"""
def Show(n=9):
    line = 13*(n-1) + 1
    print("\nMULTIPLICATION TABLE")
    print("_"*line)
    for i in range(1, 11):
        print("| ", end="")
        for j in range(2, n+1):
            print("{:<2}x{:2} = {:2}".format(j, i, j*i), end=" | ")
        print()
    print("|____________"*(n-1), end="|")
    
        
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of multiplication (2<=n<=9): ")) 
            if n < 2 and n > 9:
                raise ValueError
            break
        except:
            print("\nTry Again")
    
    Show(n)
    