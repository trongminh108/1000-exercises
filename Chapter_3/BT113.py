"""
113. Lập chương trình sin(x) với độ chính xác 0.00001 
theo công thức:

sin(x) = x - x^3/3! +...+ (-1)^n * x^(2n+1)/(2n+1)!
"""

def gt(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def Show(x):
    res = x
    previous_res = 0
    i = 1

    while abs(res - previous_res) >= 0.00001:
        previous_res = res
        res += (-1)**i * x**(2*i+1) / gt(2*i+1)
        i += 1

    return res
        
if __name__ == "__main__":
    while True:
        try:
            x = float(input("Enter your radian: "))
            break
        except:
            print("\nTry Again")

    print("Result:", Show(x))
    