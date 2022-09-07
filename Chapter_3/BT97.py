"""
Viết chương trình nhập 3 cạnh của một tam giác. 
Hãy cho biết đó là tam giác gì?
"""

from math import sqrt


def Show(a, b, c):
	if a == b and a == c:
		return "This is an equilateral triangle with side = " + str(a)
		
	if a+b>c and b+c>a and a+c>b:
		if a == b or a == c:
			return "This is an isosceles triangle"

		a *= a
		b *= b
		c *= c
		if a+b==c or a+c==b or b+c==a:
			return "This is a right triangle with hypotenuse = " + str(sqrt(max(a, b, c)))
		
	return "This is NOT a triangle"
		
if __name__ == "__main__":
	while True:
		try:
			a, b, c = map(int, input("Enter three sides of a triangle: ").split())
			break
		except:
			print("\nTry Again")
	
	print(Show(a, b, c))