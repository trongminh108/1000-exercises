"""
Hãy kiểm tra các chữ số của số nguyên dương n có tăng dần 
từ trái sang phải hay không?
"""

def BT60_Show(n):
    temp = n % 10
    n //= 10
    while n > 0:
        x = n % 10
        if temp < x:
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

    if BT60_Show(n):
        print(f"The number {n} is ascending")
    else:
        print(f"The number {n} is NOT ascending")