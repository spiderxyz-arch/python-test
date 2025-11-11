class Student:
    def __init__(self,name,mark1,mark2,):
        self.name=name
        self.mark1= mark1
        self.mark2=mark2
    def average(self):
        return self.mark1+self.mark2/2         

std1 = Student('Muhammad', 45, 85)
print(std1.average())