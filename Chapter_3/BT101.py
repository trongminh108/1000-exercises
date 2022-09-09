"""
101.Viết chương trình nhập tháng, năm. 
Hãy cho biết tháng đó có bao nhiêu ngày.
"""

from math import sqrt

def IsLeap(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

def Show(m, y):
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    names_months = ["January", "February", "March", "April", 
    "May", "June", "July", "August", "September", 
    "October", "November", "December"]
    
    if IsLeap(y):
        days_of_month[1] = 29
    return names_months[m-1], days_of_month[m-1]
    
        
if __name__ == "__main__":
    while True:
        try:
            m, y = map(int, input("Enter month and year: ").split())
            break
        except:
            print("\nTry Again")
    res = Show(m, y)
    print("The {} has {} days".format(res[0], res[1]))