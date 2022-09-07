"""
Nhập vào tháng của một năm. Cho biết tháng thuộc quí
mấy trong năm.
"""

def Show(month):
    if month <= 3:
        return 1
    if month <= 6:
        return 2
    if month <= 9:
        return 3
    return 4

if __name__ == "__main__":
    while True:
        try:
            month = int(input("Enter your month: "))
            if month < 0 or month > 12:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print(f"Tháng {month} thuộc quý {Show(month)}")