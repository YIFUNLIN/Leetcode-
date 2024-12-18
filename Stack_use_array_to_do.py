# 利用Array 實現 stack
Max = 100
stack = [None] * Max
top = -1

def isEmpty():
    if top == -1:
        return True
    else:
        return False

def push(value):
    global top
    global stack
    if top == Max -1:
        print('stack is full')
    else:
        top += 1
        stack[top] = value
    
def pop():
    global stack
    global top
    if isEmpty():
        print('stack is empty')
    else:
        print('pop value: %d'%stack[top])
        stack[top] = None
        top -= 1
    
choice = 2

while True:
    choice = int(input("Enter your choice --> 1: add value to stack、0: delete、 -1: exit :"))

    if choice == -1:
        break
    elif choice == 1:
        data = int(input("Please enter a number: "))
        push(data)
    elif choice == 0:
        pop()
    else:
        print('Invalid input')
        

print('End of program')
print('Start Erase stack')

while True:
    if top < 0:
        print('stack is empty')
        break
    else:
        print('erase value: %d'%stack[top])
        stack[top] = None
        top -= 1
