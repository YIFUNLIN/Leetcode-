# 建立一個員工資料的單向串列，並允許可在串列首、尾、中間等情況，插入新節點。
# 最後離開時，列出此串列的最後所有node的資料欄內容

import sys 

class employee:
    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ''
        self.next = None

# 定義:尋找目標Node 方法
def Find(head,num):   # num: 要插入哪個Node後的編號
    ptr = head
    while ptr != None:
        if ptr.num == num: # 剛好目前就在要的Node後面
            return ptr
        ptr = ptr.next  # 不然就一直往下找，直到找到目標Node
    return ptr

# 將 Node 插入到 Linked List 指定位置
def Insertnode(head, ptr, num, salary, name):
    # 1. 先配置好 Node 內的資訊
    Insert = employee()
    if not Insert:   # 查 ****
        return None
    Insert.num = num
    Insert.salary = salary
    Insert.name = name
    Insert.next = None
    # 2. 決定要插入的位置
    if ptr == None: # 若目前串列為空: ptr 本身為空
        Insert.next = None
        return Insert
    else:
        if ptr.next == None:  # 若ptr為最後一個Node
            ptr.next = Insert
        else:                 # 若 ptr 位在中間
            Insert.next = ptr.next
            ptr.next = Insert
    return head

position=0 # 接收使用者輸入的目標員工編號。這個編號用於決定在哪個節點後插入新的員工資訊

# 初始化資料
data=[[1001,32367],[1002,24388],[1003,27556],[1007,31299], \
      [1012,42660],[1014,25676],[1018,44145],[1043,52182], \
      [1031,32769],[1037,21100],[1041,32196],[1046,25776]]
namedata=['Allen','Scott','Marry','John','Mark','Ricky', \
          'Lisa','Jasica','Hanson','Amy','Bob','Jack']
print('員工編號 薪水 員工編號 薪水 員工編號 薪水 員工編號 薪水')
print('-------------------------------------------------------')

for i in range(3):
    for j in range(4):
        print('[%4d] $%5d '%(data[j * 3 + i][0],data[j * 3 + i][1]),end='')
    print()
print('------------------------------------------------------\n')

# 將資料寫入 Link List
head = employee() # 建立第一個空 Node
head.next = None
# 將資料寫入第一個Node
head.num = data[0][0]  # 存第一筆資料的員工編號
head.salary = data[0][1]  # 存第一筆薪水
head.name = namedata[0]   # 第一筆資料的員工姓名
head.next = None          # 第一個node 的下一個指標設為空
ptr = head                # 用ptr 指向他

# 將資料寫入剩餘的Link list中: 從第二筆資料開始，依次建立新節點
for i in range(1,12):       # 先建立11個Node
    newnode = employee()    # 初始化
    newnode.next = None     # 初始化新節點的指標
    # 開始寫入資料
    newnode.num = data[i][0]  # 儲存員工編號
    newnode.salary = data[i][1] # 儲存薪水
    newnode.name = namedata[i] # 儲存員工姓名
    newnode.next = None    # 新節點的指標初始為空

    ptr.next = newnode  # 將目前節點的 next 指向新節點
    ptr = ptr.next   # 移動 ptr 指標到新節點上


while True:
    print('請輸入要插入其後的員工編號:')
    position = int(input('新輸入的員工節點，將視為此串列的串列首，要結束請輸入-1:'))
    if position == -1:
        break
    else:
        ptr = Find(head, position)
        new_num = int(input("請輸入新插入的員工編號:"))
        new_salary = int(input("請輸入新插入的員工薪水:"))
        new_name = input("請輸入新插入的員工姓名:")
        head = Insertnode(head,ptr,new_num,new_salary,new_name)
    print()

ptr = head
print('\t員工編號   姓名\t薪水')
print('\t========================')
while ptr!=None:
    print('\t[%2d]\t[ %-7s]\t[%3d]' %(ptr.num,ptr.name,ptr.salary))
    ptr = ptr.next


