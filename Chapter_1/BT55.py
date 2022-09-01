"""
Hãy đếm số lượng chữ số đầu tiên của số nguyên dương n.
"""




def BT55_Show(n):
    s = str(n)
    count = 0
    for digit in s:
        if digit == s[0]:
            count += 1

    return count


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print("Result:", BT55_Show(n))