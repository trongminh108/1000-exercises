"""
112.Lập chương trình in ra hình chữ nhật có kích thước 
m x n. 
1. Hình chữ nhật đặc

Ví dụ: Hình chữ nhật có kích thước 7 x 4
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
"""


def Show(m, n):
    for i in range(n):
        print("* "*m)

def Other_Show(m, n):
    for i in range(n):
        for j in range(m):
            print("* ", end="")
        print()
        
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
    