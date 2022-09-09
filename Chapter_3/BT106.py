"""
106.Viết chương trình nhập vào một số nguyên có ba chữ số.
Hãy in ra cách đọc của nó.
"""

def Show(num):
    units = ["không", "một", "hai", "ba", "bốn", "năm", 
    "sáu", "bảy", "tám", "chín"]
    
    if num < 10:
        return units[num]
    
    if num % 100 == 0:
        return units[num // 100] + " trăm"

    unit_num = num % 10
    ten_num = (num // 10) % 10
    hundred_num = num // 100
    res = ""
    
    if hundred_num >= 1:
        res += units[hundred_num] + " trăm "
        if ten_num == 0:
            res += "lẻ "

    if ten_num == 1:
        res += "mười "
    elif ten_num > 1:
        res += units[ten_num] + " mươi "

    if ten_num > 1:
        units[1] = "mốt"
    units[5] = "lăm"

    if num % 10 != 0:
        res += units[unit_num]
    
    return res

def EN_Show(num):
    units = ["zero", "one", "two", "three", "four", 
    "five", "six", "seven", "eight", "nine", "ten", 
    "eleven", "twelve", "thirdteen", "fourteen", "fifteen", "sixteen", "seventeen", 
    "eighteen", "nineteen", "twenty"]

    if num <= 20:
        return units[num]

    unit_num = num % 10
    ten_num = (num // 10) % 10
    hundred_num = num // 100
    res = ""

    if hundred_num >= 1:
        res += units[hundred_num] + " hundred "
        if unit_num != 0 or ten_num != 0:
            res += "and "

    if ten_num >= 6:
        res += units[ten_num] + "ty " 
    elif ten_num >= 5:
        res += "fifty "
    elif ten_num >= 4:
        res += "forty "
    elif ten_num >= 3:
        res += "thirdty "
    elif ten_num >= 2:
        res += units[20] + " "
    elif ten_num >= 1:
        res += units[num % 100] + " "

    if num % 10 != 0 and ten_num != 1:
        res += units[unit_num]

    return res
        
if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter number from 000 -> 999: "))
            if num < 0 or num > 999:
                raise ValueError
            break
        except:
            print("\nTry Again")

    print(f"Số {num} đọc là:", Show(num))
    print(f"{num} reads as:", EN_Show(num))
    
    