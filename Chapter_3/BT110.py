"""
109.Viết chương trình in bảng cửu chương ra màn hình.
"""

from time import time

def Show(money=200000):
    one = money // 1000
    two = money // 2000
    five = money // 5000
    res = []

    for k in range(five+1):
        for j in range(two+1):
            temp = 5000*k + 2000*j
            if temp <= money:
                i = (money-temp) // 1000
                res.append((i, j, k))

    return res
    
        
if __name__ == "__main__":
    while True:
        try:
            money = int(input("Enter money: ")) 
            if money < 1000 or money % 1000 != 0:
                raise ValueError
            break
        except:
            print("\nTry Again")
    start = time()
    res = Show(money)
    for val in res:
        print(val)
    print(len(res))
    print("Time:", time()-start)
    