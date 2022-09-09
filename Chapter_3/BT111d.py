"""
Viết chương trình in ra tam giác cân có độ cao h.
d. Tam giác vuông cân rỗng
Ví dụ với h = 5
*
* *
*   *
*     *
* * * * *
"""


def Show(n):
    k = 1
    for i in range(1, n+1):
        if i == 1 or i == n:
            print("* "*i)
        else:
            print("*" + " "*k + "*")
            k += 2

def Other_Show(n):
    k = 1
    for i in range(1, n+1):
        if i == 1 or i == n:
            for j in range(i):
                print("* ", end="")
            print()
        else:
            print("*", end="")
            for i in range(k):
                print(" ", end="")
            print("*")
            k += 2
        
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
    print()
    Other_Show(n)
    