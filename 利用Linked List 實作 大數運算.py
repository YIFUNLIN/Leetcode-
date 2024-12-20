# 113 交大資財所: 利用Linked List 實作 大數運算
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
def BN_new():
    return None

def BN_insert(head, digit):  # 要知道目前head指向誰，跟插入的數值
    new_node = Node(digit) # 先替新數字建一個新node
    
    # 再由head來判斷該Linked List 有無其他Node
    if head == None:  # 若head為空，代表是空串列
        return new_node   # 直接回傳該 Node
    
    # 若有
    current = head  # 用current 先指向該Linked List 的head 
    while current.next != None: # 當他還不是最後一個 node，就一直走到最後一個node
        current = current.next
    current.next = new_node # 將新Node 接在最後一個Node 後面
    return head  # 回傳整個Linked List

def reverse(head):  # 為了要實現Linked List 的相加，所以先將整個Linked List 反轉
        prev = None    
        while head:
            next_node = head.next  # 先用另一個指標 next_node，指向 head 的下一個node
            head.next = prev       # 改變 head 的 next 去指向 prev 所在 (為了完成反轉)
            prev = head            # prev 往前來到 head 位置
            head = next_node       # head 往前來到 next_node 位置
        return prev                # 最後回傳反轉完的 Linked List


def BN_add(A,B,C):   
    A, B = reverse(A), reverse(B)  # 反轉兩個Linked List
        
    # 計算過程
    carry = 0  # 若有需要進位，則放在這
    
    # 建立存放答案 C 的 Linked List
    result_tail = None  # 動態追蹤尾部並新增節點

    # 遍歷Linked List
    while A or B or carry:
        val1 = A.val if A else 0
        val2 = B.val if B else 0
    
        # 計算當前總和
        total = val1 + val2 + carry
        carry = total // 10  # 計算看是否進位，取得當前的進位
        digit = total % 10   # 餘數: 要先將餘數插入到 Node 中
        
        # 建立新的 Node 來存放這次運算完的結果
        new_node = Node(digit)
        
        if C == None:  # 若為空串列
            C = new_node  # 將head指向該Node
            result_tail = new_node   # tail 跑去該node位置
        else:
            result_tail.next = new_node   
            result_tail = new_node
            
        # 往下走
        A = A.next if A else None
        B = B.next if B else None
    return reverse(C)  # 將Linked List 結果反轉回去才是正確的順序
    
    
def BN_print(head):    # 之後會將C傳入，要印出來用
    ans = []           # 建立空列表
    while head != None:
        ans.append(str(head.val))  # 將每個值轉成字串後存入
        head = head.next    
    return ''.join(ans)

# ============== 以下為測試 =================
A = BN_new()
B = BN_new()
C = BN_new()

for i in range(9,0,-1):
    A = BN_insert(A,i)
for i in range(0,8,1):
    B = BN_insert(B,8)
C = BN_add(A,B,C)
print(BN_print(C))
    
    BN_print(C)
