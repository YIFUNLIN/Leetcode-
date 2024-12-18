# Stack 使用 Link List 實作
class Node:
    def __init__(self):
        self.data = 0
        self.next = None
        
top = None

def isEmpty():
    if top == None:
        return True
    else:
        return False
    
def push(value):
    global top
    new_node = Node()
    new_node.data = value
    new_node.next = top
    top = new_node
    
def pop():
    global top
    if isEmpty():
        print('stack is empty')
    else:
        ptr = top
        top = top.next  # 在執行push時, top 會指向Node 所以就可以用.next 來取得下一個Node
        temp = ptr.data  # 從Stack 取出頂端的資料(最後一個Node的data)
        return temp
    
while True:
    choice = int(input("Enter your choice:  1: add value to stack    0: delete      -1: exit :"))
    if choice == -1:
        break
    elif choice == 1:
        data = int(input("Please enter a number: "))
        push(data)
    elif choice == 0:
        print('pop value: %d'%pop())
    else:
        print('Invalid input')
    
print('================================================================')
print('End of program')
print("Erase stack")
while (not isEmpty()):
    print('erase value: %d'%pop())
