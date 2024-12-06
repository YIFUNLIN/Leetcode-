# Leetcode: 622. Design Circular Queue
#-----------------------------------------------------------------------------------------------------
# 法一. 使用Circular array 但只利用了(n-1)格
class MyCircularQueue:

    def __init__(self, k: int):
        # 初始化佇列屬性
        self.size = k + 1  # 留一格空間
        self.array = [0] * self.size
        self.front = 0  # 指向佇列的第一個元素
        self.rear = 0   # 指向佇列的下一個插入位置

    def enQueue(self, value: int) -> bool:
        # 插入元素
        next_rear = (self.rear + 1) % self.size  # 計算新的 rear 位置
        if next_rear == self.front:  # 如果滿了
            print("Queue is Full")
            return False
        self.array[self.rear] = value
        self.rear = next_rear  # 更新 rear
        return True

    def deQueue(self) -> bool:
        # 刪除元素
        if self.front == self.rear:  # 如果空了
            print("Queue is Empty")
            return False
        self.front = (self.front + 1) % self.size  # 更新 front
        return True  # 返回 True 表示成功刪除

    def Front(self) -> int:
        # 返回佇列的第一個元素
        if self.front == self.rear:  # 如果空了
            return -1
        return self.array[self.front]

    def Rear(self) -> int:
        # 返回佇列的最後一個元素
        if self.front == self.rear:  # 如果空了
            return -1
        return self.array[(self.rear - 1 + self.size) % self.size]

    def isEmpty(self) -> bool:
        # 判斷佇列是否空
        return self.front == self.rear

    def isFull(self) -> bool:
        # 判斷佇列是否滿
        return (self.rear + 1) % self.size == self.front


#------------------------------------------------------------------------------------------------------
# 法二. 使用Circular array 利用了所有格:n
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








