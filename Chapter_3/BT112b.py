"""
112.Lập chương trình in ra hình chữ nhật có kích thước 
m x n. 
b) Hình chữ nhật rỗng
Ví dụ: Hình chữ nhật có kích thước 7 x 4
* * * * * * *
*           *
*           *
* * * * * * *
"""


def Show(m, n):
    for i in range(n):
        if i == 0 or i == n-1:
            print("* "*m)
        else:
            print("* " + "  "*(m-2) + "*")

def Other_Show(m, n):
    for i in range(n):
        if i == 0 or i == n-1:
            for j in range(m):
                print("* ", end="")
            print()
        else:
            print("* ", end="")
            for i in range(m-2):
                print("  ", end="")
            print("*")

        
if __name__ == "__main__":
    while True:
        try:
            m, n = map(int, input("Enter length and width of rectangle: ").split())
            if n <= 0 or m <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again")

    Show(m, n)
    print()
    Other_Show(m, n)
    