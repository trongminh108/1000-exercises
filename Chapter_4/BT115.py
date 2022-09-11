"""
115.Viết chương trình nhập họ tên, điểm toán, 
điểm văn của một học sinh. 
Tính điểm trung bình và xuất kết quả
"""

class Student:
    def __init__(self, name="", math=0.0, lecture=0.0) -> None:
        self.__name = name
        self.__math = math
        self.__lecture = lecture
    
    def Calculate(self):
        return (self.__math + self.__lecture) / 2

    def __str__(self) -> str:
        return self.__name + " " + str(self.Calculate())

def Show():
    st = Student("Luu Minh Trong", 6.5, 7.5)
    st2 = Student("Trong Minh", 8, 9)
    st3= Student("Jame Luu", 10, 8)

    print(st)
    print(st2)
    print(st3)
        
if __name__ == "__main__":
    Show()
    