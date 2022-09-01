"""
Hãy kiểm tra số nguyên dương n có toàn chữ số chẵn hay 
không?
"""

def BT57_Show(n):
    while n > 0:
        if n % 2:
            return False
        n //= 10
    return True


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    if BT57_Show(n):
        print(f"The number {n} is full of even digits")
    else:
        print(f"The number {n} has at least one odd digit")