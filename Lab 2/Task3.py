
# simple function 

def function():
    print("shahzaib")

function()

# function with the parameter 

def func(temp):
    print("hello"+" "+temp)

func("shah")

# function with the return

def func(temp):
    return("hello"+" "+temp)

print(func("Arif"))

# function with the keywords

def keyw(name,gpa):
    print(f"My name is {name} and my GPA is {gpa}")

keyw("Ahmad",3.94)  

# function with default parameter

def defaul(name="hassam",rollno="ybvf"):
    print(f"My name is {name} and my Roll no is {rollno}")

defaul("hello")


# Passing list as a parameter 

def listfunc(list):
    for i in list:
        print(i)

listt=["cat","dog","horse"]

listfunc(listt)



