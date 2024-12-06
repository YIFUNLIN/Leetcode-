# Leetcode: 622. Design Circular Queue
#-----------------------------------------------------------------------------------------------------
# 法一. 使用Circular array 利用 n 個 array <最直觀的做法 讚!>
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.array = [0] * self.size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.size:
            print('Queue is Full')
            return False
        self.array[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            print('Queue is empty')
            return False
        self.array[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.array[self.front]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.array[(self.rear - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.count == 0
        
    def isFull(self) -> bool:
        return self.count == self.size

# 法二. 使用Circular array 但只利用了(n-1)格
class MyCircularQueue:
    def __init__(self, k: int):
        # Initialize the circular queue: with size use k+1 to identify
        self.size = k + 1  # 多留一個空間給front
        self.array = [0] * self.size  # 配置給queue 對應的空間
        self.front = 0  # 指向queue的第一個元素
        self.rear = 0   # 指向queue下一個要插入的位置

    def enQueue(self, value: int) -> bool:
        next_rear = (self.rear + 1) % self.size # 先計算新的 rear 位置:指向下一個要存放的address
        if next_rear == self.front:  # 如果下一個要存的位址=Queue的第一個元素
            print('Queue is Full')
            return False             # 代表此Queue已滿
        self.array[self.rear] = value  # 若Queue沒滿，將值插入到rear位置 
        self.rear = next_rear    # 更新rear 的 address
        return True
    
    def deQueue(self) -> bool:
        if self.front == self.rear:
            print('Queue is empty')
            return False
        self.front = (self.front + 1) % self.size # 更新front: 往後走一格，表示此位置已刪除
        return True    

    def Front(self) -> int:
        # 返回queue中的第一個元素
        if self.front == self.rear:
            return -1 # 表示queue 中沒有符合的
        return self.array[self.front] # 若queue不為空，可以直接回傳front位置，他一定指向第一個元素

    def Rear(self) -> int:
        if self.front == self.rear:  # 如果佇列為空
            return -1
        # 正確計算最後一個有效元素的位置
        return self.array[(self.rear - 1 + self.size) % self.size]


    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front



#------------------------------------------------------------------------------------------------------
# 法三. 使用Circular array 利用了所有格:n
class MyCircularQueue:

    def __init__(self, k: int):
        # 初始化佇列屬性
        self.size = k
        self.array = [0] * k  # 陣列儲存數據
        self.front = 0  # 指向佇列的第一個元素
        self.rear = 0   # 指向佇列的下一個插入位置
        self.tag = 0    # 用於區分「滿」與「空」的標記

    def enQueue(self, value: int) -> bool:
        # 插入元素
        if self.front == self.rear and self.tag == 1:  # 判斷佇列是否滿
            print("Queue is Full")
            return False
        self.array[self.rear] = value
        self.rear = (self.rear + 1) % self.size  # 循環更新 rear
        if self.rear == self.front:  # 如果 rear 繞回到 front，設置 tag=1
            self.tag = 1
        return True

    def deQueue(self) -> bool:
        # 刪除元素
        if self.front == self.rear and self.tag == 0:  # 判斷佇列是否空
            print("Queue is Empty")
            return False
        data = self.array[self.front]
        self.front = (self.front + 1) % self.size  # 循環更新 front
        if self.front == self.rear:  # 如果 front 繞回到 rear，設置 tag=0
            self.tag = 0
        return True

    def Front(self) -> int:
        # 返回佇列的第一個元素
        if self.front == self.rear and self.tag == 0:  # 判斷佇列是否空
            return -1
        return self.array[self.front]

    def Rear(self) -> int:
        # 返回佇列的最後一個元素
        if self.front == self.rear and self.tag == 0:  # 判斷佇列是否空
            return -1
        return self.array[(self.rear - 1 + self.size) % self.size]

    def isEmpty(self) -> bool:
        # 判斷佇列是否空
        return self.front == self.rear and self.tag == 0

    def isFull(self) -> bool:
        # 判斷佇列是否滿
        return self.front == self.rear and self.tag == 1








