"""
Viết chương trình in ra tất cả các số lẻ nhỏ hơn 100 
trừ các số 5, 7, 93.
"""


def Show(n=100):
    res = []
    for i in range(1, n+1, 2):
        if i == 5 or i == 7 or i == 93:
            continue
        res.append(str(i))
    return ", ".join(res)

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter a number: "))
            break
        except:
            print("\nTry Again")

    print(Show(n))
        