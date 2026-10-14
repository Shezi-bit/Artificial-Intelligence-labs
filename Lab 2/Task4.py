#class
class first:
    name = "Shahzaib"
    rollno = 16

x = first()
print(x.name)
print(x.rollno)

# def init
class second:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.dep=z

    def func(self):
        print(f"name is {self.name} roll no is {self.rollno} and dep is {self.dep}")

x = second("abc",4,"IT")
x.func()
print(x.name)