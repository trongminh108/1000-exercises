"""
64. Giải phương trình ax + b = 0.
"""



def BT64_Show(string):
    list_nums = list(string+"@")
    res = []
    count = -1
    i = 0
    while i < len(list_nums):
        if list_nums[i].isnumeric():
            res.append(list_nums[i])
            count += 1
            while list_nums[i+1].isnumeric() or list_nums[i+1].lower() == "x":
                i += 1
                res[count] += list_nums[i].lower()
        i += 1
    return Solution(res)

def Solution(parameters):
    bc = []
    a = 0
    for num in parameters:
        if "x" in num:
            a = int(num[:-1])
        else:
            bc.append(int(num))
    b = bc[0] - bc[1]
    return -b/a

if __name__ == "__main__":
    while True:
        try:
            string = input("Enter your first degree equation: ")
            break
        except:
            print("\nTry Again!")

    print(f"The result x of {string} is x = {BT64_Show(string)}")
