"""
Viết chương trình giải phương trình bậc 2.
"""

from math import sqrt


def Show(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "This equation has NO solution"
            return "This equation has INFINITELY MANY solutions"
        return -c/b

    delta = b*b - 4*a*c
    if delta < 0:
        return "This equation has NO solution"

    x1 = (-b - sqrt(delta)) / (2*a)
    x2 = (-b + sqrt(delta)) / (2*a)

    if x1 == x2:
        return x1
    return x1, x2

    
		
if __name__ == "__main__":
	while True:
		try:
			a, b, c = map(int, input("Enter three numbers of the quadratic equation: ").split())
			break
		except:
			print("\nTry Again")
	
	print("Result:", Show(a, b, c))
	