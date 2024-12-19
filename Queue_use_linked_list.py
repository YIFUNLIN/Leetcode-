# Queue 使用Linked list 實作
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear == None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        # 若最前面沒有節點
        if self.front == None:
            print("Queue is empty")
            return None
        # 若還有節點
        dequeue_data = self.front.data # 先取出front 位置的值
        self.front = self.front.next # 往後走一個節點
        if self.front == None:   # 再判斷一次front 是否為空
            self.rear = None    
        return dequeue_data
    
    def is_empty(self):
        return self.front == None
    
    def peek(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        return self.front.data
    
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())  # 輸出: 10
print(queue.dequeue())  # 輸出: 20

# 查看頭部元素
print(queue.peek())     # 輸出: 30

# 檢查是否為空
print(queue.is_empty())  # 輸出: False

# 繼續取出
print(queue.dequeue())  # 輸出: 30
print(queue.is_empty())  # 輸出: True

# 嘗試從空隊列取出
print(queue.dequeue())  # 輸出: Queue is empty
