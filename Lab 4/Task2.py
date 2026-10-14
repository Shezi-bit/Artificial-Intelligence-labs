stack = []
 
 # push function 

def push(val):
    stack.append(val)

# pop function

def pop(stack):
    # remove values: from the front (index 0)
    if len(stack)==0:
        print("No Value")
    else:
        print(stack.pop())

# add values

push(1)
push(2)
push(3)
push(4)
push(5)

print(stack)

pop(stack)
