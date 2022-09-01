"""
Hãy kiểm tra số nguyên dương n có phải số đối xứng hay 
không?
"""

def BT59_Show(n):
    list_digits = []
    while n > 0:
        list_digits.append(n%10)
        n //= 10
    lgt = len(list_digits)
    for i in range(lgt//2):
        if list_digits[i] != list_digits[lgt-i-1]:
            return False
    return True

def SymmetricNumber(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter positive number n: "))
            if n <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    if BT59_Show(n) and SymmetricNumber(n):
        print(f"The number {n} is symmetric number")
    else:
        print(f"The number {n} is NOT symmetric number")