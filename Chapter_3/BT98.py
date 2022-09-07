"""
Lập chương trình giải hệ:
    ax + by = c
    dx + ey = f
"""

from fractions import Fraction


def Show(f1, f2):
    if f1[1] != f2[1]:
        b = f1[1]
        f1 = [i*f2[1] for i in f1]
        f2 = [i*b for i in f2]

    temp = []
    for i in range(len(f1)):
        temp.append(f1[i]-f2[i])
    
    x = temp[2] / temp[0]
    y = (f1[2] - f1[0]*x) / f1[1]

    return x, y
    
		
if __name__ == "__main__":
	while True:
		try:
			f1 = input("Enter three numbers of f1: ").split()
			f2 = input("Enter three numbers of f2: ").split()
			if len(f1)==3 and len(f2)==3:
				f1 = [int(i) for i in f1]
				f2 = [int(i) for i in f2]
			else:
				raise ValueError
			break
		except:
			print("\nTry Again")
	
	print("Result:", Show(f1, f2))