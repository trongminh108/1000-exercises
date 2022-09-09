"""
Viết chương trình in ra tam giác cân có độ cao h.
a. Tam giác cân đặc nằm giữa màn hình.
Ví dụ với h = 4
      *
    * * *
  * * * * *
* * * * * * *
"""


def Show(n):
    i = 1
    for row in range(1, n+1):
        print("  "*(n-row) + "* "*i)
        i += 2

def Other_Show(n):
    k = 1
    for row in range(n):
        for col in range(row, n-1):
            print("  ", end="")
        
        for col in range(k):
            print("* ", end="")
        
        k += 2
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
    