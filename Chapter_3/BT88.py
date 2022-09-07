"""
Hãy sử dụng vòng lặp for để xuất tất cả các ký tự A tới Z.
"""

def Show():
    res = []
    for i in range(0, 26):
        res.append(chr(65+i))
    return ", ".join(res)

if __name__ == "__main__":
    print("A -> Z:",Show())
    