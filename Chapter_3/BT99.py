"""
Viết chương trình nhập vào 3 số thực. Hãy in 3 số thực 
ấy ra màn hình theo thứ tự tăng dần mà chỉ dùng tối đa 
hai biến phụ.
"""

def Show(a, b, c):
	d = a if a < b else b
	e = a if a >= b else b

	if c >= d:
		d, c = c, d
		if d >= e:
			d, e = e, d

	return c, d, e
		
if __name__ == "__main__":
	while True:
		try:
			a, b, c = map(int, input("Enter three numbers: ").split())
			break
		except:
			print("\nTry Again")
	
	print("Result:", Show(a, b, c))
	