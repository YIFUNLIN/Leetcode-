import sys
import random

def concatlist(ptr1,ptr2):  # 連接兩個single link list
    ptr = ptr1
    while ptr.next != None:
        ptr = ptr.next
    ptr.next = ptr2
    return ptr1

class employee:
    def __init__(self):
        self.num = 0
        self.name = ''
        self.salary = 0
        self.next = None

namedata1=['Allen','Scott','Marry','Jon', \
          'Mark','Ricky','Lisa','Jasica', \
          'Hanson','Amy','Bob','Jack']

namedata2=['May','John','Michael','Andy', \
          'Tom','Jane','Yoko','Axel', \
          'Alex','Judy','Kelly','Lucy']

# 先個別用兩個Link List 去儲存資料
data = [[None]*2 for i in range(12)]

# 第一個Link List
for i in range(12):
    data[i][0] = i+1
    data[i][1] = random.randint(51,100)

head1 = employee()
head1.name = namedata1[0]
head1.num = data[0][0]
head1.salary = data[0][1]
head1.next = None
ptr = head1

for i in range(1,12): # 遍歷剩餘的11筆，將資料寫入
    newnode = employee()
    newnode.name = namedata1[i]
    newnode.num = data[i][0]
    newnode.salary = data[i][1]
    newnode.next = None

    ptr.next = newnode
    ptr = ptr.next


# 第二個Link List
for i in range(12):
    data[i][0] = i+13  # 索引值從13開始
    data[i][1] = random.randint(51,100)

# 先單獨處理第一個Node    
head2 = employee()
head2.num = data[0][0]
head2.name = namedata2[0]
head2.salary = data[0][1]
head2.next = None

ptr = head2

for i in range(1,12):
    newnode = employee()
    newnode.name = namedata2[i]
    newnode.num = data[i][0]
    newnode.salary = data[i][1]
    newnode.next = None
    ptr.next = newnode
    ptr = ptr.next

# 串接兩個Link List
ptr = concatlist(head1,head2)
print('兩個Link list 相連結果:')

# 控制輸出的格式，以便將鏈結串列的內容按照每行三個節點的方式排列
i = 0 # 用來記錄輸出Node的數量
while ptr != None:
    print('[%2d %6s %3d] => ' %(ptr.num, ptr.name, ptr.salary),end='')
    i = i + 1
    if i >= 3: 
        print() # 換行
        i = 0   # 歸 0，重新計算
    ptr = ptr.next

