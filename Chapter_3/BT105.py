"""
105.Viết chương trình nhập một số nguyên có hai chữ số. 
Hãy in ra cách đọc của số nguyên này
"""

def Show(num):
    donvi = ["không", "một", "hai", "ba", "bốn", "năm", 
    "sáu", "bảy", "tám", "chín"]
    chuc = ["mười", "mươi"]
    
    if num == 0:
        return donvi[num]

    unit_num = num % 10
    ten_num = num // 10
    if ten_num >= 1 and unit_num == 5:
        donvi[unit_num] = "lăm"
    res = ""
    if ten_num == 1:
        res = chuc[0] + " "
    elif ten_num > 1:
        res = donvi[ten_num] + " " + chuc[1] + " "

    if num % 10 != 0:
        res += donvi[unit_num]
    
    return res

def EN_Show(num):
    units = ["zero", "one", "two", "three", "four", 
    "five", "six", "seven", "eight", "nine", "ten", 
    "eleven", "twelve", "thirdteen", "fourteen", "fifteen", "sixteen", "seventeen", 
    "eighteen", "nineteen", "twenty", "thirdty"]

    ten_num = num // 10
    unit_num = num % 10
    res = ""

    if num <= 20:
        return units[num]
    elif num < 30:
        res = units[20] + " "
    elif num < 40:
        res = units[21] + " "
    else:
        if ten_num != 5:
            res = units[ten_num] + "ty "
        else:
            res = "fifty "

    if num % 10 != 0:
        res += units[unit_num]

    return res

        
if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter number from 00 -> 99: "))
            if num < 0 or num > 99:
                raise ValueError
            break
        except:
            print("\nTry Again")

    print(f"Số {num} đọc là:", Show(num))
    print(f"{num} reads as:", EN_Show(num))
    
    