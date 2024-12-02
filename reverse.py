class employee:
    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ''
        self.next = None


def invert_list(head):
    last = None
    before = None
    ptr = head
    while ptr != None:
        last = before    # 保存前一個節點 (r = q)
        before = ptr     # 更新當前節點為反轉後的新頭部 (q = p)
        ptr = ptr.next   # 移動到下一個節點 (p = p.next)
        before.next = last  # 反轉指向 (q.next = r)
    return before

# 初始化資料
namedata = ['Allen', 'Scott', 'Marry', 'Jon',
            'Mark', 'Ricky', 'Lisa', 'Jasica',
            'Hanson', 'Amy', 'Bob', 'Jack']

data = [[1001, 32367], [1002, 24388], [1003, 27556], [1007, 31299],
        [1012, 42660], [1014, 25676], [1018, 44145], [1043, 52182],
        [1031, 32769], [1037, 21100], [1041, 32196], [1046, 25776]]

# 建立鏈結串列
head = employee()  # 建立串列首
head.num = data[0][0]
head.name = namedata[0]
head.salary = data[0][1]
head.next = None
ptr = head

for i in range(1, 12):  # 建立鏈結串列
    newnode = employee()
    newnode.num = data[i][0]
    newnode.name = namedata[i]
    newnode.salary = data[i][1]
    newnode.next = None
    ptr.next = newnode
    ptr = ptr.next

# 列印原始串列
ptr = head
i = 0
print('原始員工串列節點資料：')
while ptr is not None:  # 列印串列資料
    print('[%2d %6s %3d] => ' % (ptr.num, ptr.name, ptr.salary), end='')
    i += 1
    if i >= 3:  # 每三個元素為一列
        print()
        i = 0
    ptr = ptr.next

# 反轉串列
head = invert_list(head)

# 列印反轉後的串列
ptr = head
i = 0
print('\n反轉後串列節點資料：')
while ptr != None:
    print('[%2d %6s %3d] => ' % (ptr.num, ptr.name, ptr.salary), end='')
    i += 1
    if i >= 3:
        print()
        i = 0
    ptr = ptr.next
