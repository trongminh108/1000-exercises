"""
104.Viết chương trình nhập vào ngày, tháng, năm. 
Tính xem ngày đó là ngày thứ bao nhiêu trong năm.
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
    
    days = d
    for i in range(m-1):
        days += days_of_month[i]
    
    return days
        
if __name__ == "__main__":
    while True:
        try:
            d, m, y = map(int, input("Enter day, month and year: ").split())
            break
        except:
            print("\nTry Again")
    
    res = Show(d, m, y)
    day = ["st", "nd", "rd", "th"]
    if res < 4:
        s = day[res-1]
    else:
        s = "th"
    print(f"The day {d:02d}/{m:02d}/{y:04d} is the {res}{s} day")