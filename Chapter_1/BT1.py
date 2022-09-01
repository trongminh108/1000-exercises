"""
Tính S(n) = 1 + 2 + 3 + … + n
"""

try:
    n = int(input("Nhap so nguyen n: "))
except:
    print("Ban da nhap sai dinh dang!")

sum = 0
lst = []
for i in range(1, n+1):
    lst.append(str(i))
    sum += i
out_put = " + ".join(lst)
print(out_put + " = " + str(sum))