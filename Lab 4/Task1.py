queue = []
 
 # push function 

def push(val):
    queue.append(val)

# pop function

def pop(queue):
    # remove values: from the front (index 0)
    if len(queue)==0:
        print("No Value")
    else:
        print(queue.pop(0))

# add values

push(1)
push(2)
push(3)
push(4)
push(5)

print(queue)

pop(queue)






    



  