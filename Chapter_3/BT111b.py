"""
Viết chương trình in ra tam giác cân có độ cao h.
b. Tam giác cân rỗng nằm giữa màn hình.
Ví dụ với h = 4
      *
    *   *
  *       *
* * * * * * *
"""


def Show(n):
    i = 1
    k = 3
    for row in range(1, n+1):
        print("  "*(n-row), end="")
        if row == n:
            print("* "*i)
        elif row != 1:
            print("*" + " "*k + "*")
            k += 4
        else:
            print("*")
        i += 2

def Other_Show(n):
    k = 1
    j = 3
    for row in range(n-1):
        for col in range(row, n-1):
            print("  ", end="")

        if row == 0:
            print("*")
        else:
            print("*", end="")
            for i in range(j):
                print(" ", end="")
            print("*")
            j += 4
        k += 2

    for i in range(k):
        print("* ", end="")
    print()

        
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the height of isosceles: ")) 
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again")

    Show(n)
    Other_Show(n)
    