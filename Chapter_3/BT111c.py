"""
Viết chương trình in ra tam giác cân có độ cao h.
c. Tam giác vuông cân đặc
Ví dụ với h = 4
*
* *
* * *
* * * *
"""


def Show(n):
    for i in range(1, n+1):
        print("* "*i)

def Other_Show(n):
    for i in range(1, n+1):
        for j in range(i):
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
    