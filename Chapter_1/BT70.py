"""
70. Tính S(n) = 1 - 1/(1+2) + 1/(1+2+3) -...+ (-1)^(n+1)*1/(1+2+...+n)
"""
def sum(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

def BT70_Show(n):
    res = 0
    for i in range(1, n+1):
        res += (-1)**(i+1) * 1/(sum(i))
    return res


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter number n: "))
            break
        except:
            print("\nTry Again!")

    print("Result:", BT70_Show(n))
