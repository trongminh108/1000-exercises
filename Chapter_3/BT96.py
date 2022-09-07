"""
96. Viết chương trình nhập giá trị x sau khi tính giá trị 
của hàm số:
f(x) = {
2x^2 + 5x + 9 khi x>= 5
-2x^2 + 4x - 9 khi x < 5
"""

def Show(n):
	f1 = lambda x: 2*x**2 + 5*x + 9
	f2 = lambda x: (x**2)*(-2) + 4*x - 9
	if n >= 5:
		return f1(n)
	else:
		return f2(n)
		
if __name__ == "__main__":
	while True:
		try:
			n = int(input("Enter a number n: "))
			break
		except:
			print("\nTry Again")
	
	print("Result:", Show(n))