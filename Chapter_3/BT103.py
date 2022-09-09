"""
103.Viết chương trình nhập vào một ngày (ngày, tháng, năm). Tìm ngày
trước ngày vừa nhập (ngày, tháng, năm).
"""

from math import sqrt

def IsLeap(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

def Show(d, m, y):
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    names_months = ["January", "February", "March", "April", 
    "May", "June", "July", "August", "September", 
    "October", "November", "December"]
    
    if IsLeap(y):
        days_of_month[1] = 29
    
    d -= 1
    if d == 0:
        m -= 1
        if m == 0:
            m = 12
            y -= 1
        d = days_of_month[m-1]
    
    return d, names_months[m-1], y
        
if __name__ == "__main__":
    while True:
        try:
            d, m, y = map(int, input("Enter day, month and year: ").split())
            break
        except:
            print("\nTry Again")
    res = Show(d, m, y)
    print(f"The next day is {res[0]:02d} - {res[1]:s} - {res[2]:04d}")