# 允許刪除 串列首、中或最後的 Node
class employee:
    def __init__(self):
        self.num = 0
        self.name = ''
        self.salary = 0
        self.next = None

# 刪除 Node 程式
def del_ptr(head, ptr):  # head：鏈結串列的起始節點（頭部）、ptr：需要刪除的目標節點
    top = head
    if ptr.num == head.num:  # Case1: 若要刪除的Node在頭
        head = head.next
        print('已刪除第 %d 號員工 姓名:%s 薪資:%d'%(ptr.num,ptr.name,ptr.salary))
    else:
        while top.next != ptr:  
            top = top.next     # 遍歷找到目標節點的前一個節點
        if ptr.next == None:   # 若 ptr 是最後一個Node
            top.next = None    # 將前一個節點的 next 直接設為 None
            print('已刪除第 %d 號員工 姓名:%s 薪資:%d'%(ptr.num,ptr.name,ptr.salary))
        else:
            top.next = ptr.next   # 刪除中間節點：跳過目標節點
            print('已刪除第 %d 號員工 姓名:%s 薪資:%d'%(ptr.num,ptr.name,ptr.salary))
    return head

def main():
    namedata=['Allen','Scott','Marry','John',\
              'Mark','Ricky','Lisa','Jasica',\
              'Hanson','Amy','Bob','Jack']
    data=[[1001,32367],[1002,24388],[1003,27556],[1007,31299], \
          [1012,42660],[1014,25676],[1018,44145],[1043,52182], \
          [1031,32769],[1037,21100],[1041,32196],[1046,25776]]
    print('員工編號 薪水 員工編號 薪水 員工編號 薪水 員工編號 薪水')
    print('-------------------------------------------------------')
    for i in range(3):
        for j in range(4):
            print('%2d [%3d] '%(data[j*3 + i][0],data[j*3 + i][1]),end='')
        print()
    
    # 初始化
    head = employee()

    # 先將第一筆資料寫入 Node 
    head.num = data[0][0]
    head.salary = data[0][1]
    head.name = namedata[0]
    head.next = None

    ptr = head 

    # 將剩餘資料寫入 Link List
    for i in range(1,12):
        newnode = employee()
        newnode.num = data[i][0]
        newnode.salary = data[i][1]
        newnode.name = namedata[i]
        newnode.next = None
        ptr.next = newnode # 先建立與新 Node 連線
        ptr = ptr.next  # 再將 ptr 指向新的 Node 

    while(True):
        goal = int(input('請輸入要刪除的員工編號，要跳出請輸入-1:'))
        if (goal == -1):
            break
        else:
            ptr = head
            find = 0
            while ptr != None:
                if ptr.num == goal:
                    ptr = del_ptr(head, ptr) # 更新 head
                    find += 1
                    break  # 停止遍歷
                ptr = ptr.next
            if find == 0:
                print('沒找到')
            
            ptr = head
            print('\t座號\t    姓名\t成績')   #列印剩餘串列資料
            print('\t==============================')
            while(ptr!=None):
                print('\t[%2d]\t[ %-10s]\t[%3d]' %(ptr.num,ptr.name,ptr.salary))
                ptr=ptr.next
main()
