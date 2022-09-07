"""
Tính S(n) = 1^3 + 2^3 + 3^3 + … + n^3.
"""

def Show(n):
    return sum([i**3 for i in range(1, n+1)])

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter number n: "))
            break
        except:
            print("\nTry Again!")

    print(f"The sum from 1**3 to {n}**3 is {Show(n)}")