# 113 交大資財所: 利用Linked List 實作 大數運算
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def BN_new():              # 初始化空Linked List
        return None

def BN_insert(head,digit):
    new_node = Node(digit)  # 建立一個新 Node
    
    # 先判斷該Linked List 有無其他 Node
    if head == None:   # 若 head 為空，代表是空串列
        return new_node  # 回傳該新 Node  
    
    # 若非空串列
    current = head  #  先讓 current 指向head
    while current.next: # 讓current 找到最後一個node
        current = current.next
    current.next = new_node # 將新Node 接在最後一個Node 後面
    return head  # 回傳整個Linked List
    
def BN_add(A, B):
    def reverse(head):  # 因為Linked List 要從尾端刪除不易運算，所以直接先將整個反轉過來
        prev = None
        while head:
            next_node = head.next  # 先設一個指標指向head的下一個node
            head.next = prev  # 將head的next 指向prev 所在 (為了完成反轉)
            prev, head = head, next_node # 指標往前進
        return prev 
    
    A, B = reverse(A), reverse(B) # 反轉兩個Linked List
    
    carry = 0   # 若有需要進位，則放在這
    result_head = None
    
    while A or B or carry:  
        val1 = A.val if A else 0
        val2 = B.val if B else 0
    
        # 計算當前總和    
        total = val1 + val2 + carry
        
        # 計算進位和當前位數
        carry = total // 10  # 計算看是否進位，取得當前的進位
        digit = total % 10   # 取得當前的個位數
        
        # 這邊開始建立新的Linked List: C 用來存相加完的結果
        # 創建新 Node 並插入到 head
        new_node = Node(digit)
        
        # 這邊針對Linked List: C做反轉，因為剛剛反轉過，現在要轉回來才正確
        new_node.next  = result_head 
        result_head = new_node
        
        A = A.next if A else None
        B = B.next if B else None
    return result_head
    
        

def BN_print(head):  # 之後會將C傳入，要印出來用
    result = [] # 建立空列表
    while head:
        result.append(str(head.val)) # 將每個值轉成字串後存入
        head = head.next
    print("".join(result))
        
    
# ========= 主程式測試 ================

if __name__ == '__main__':
    A = BN_new()
    for i in range(9,0,-1):
        A = BN_insert(A, i)
    B = BN_new()
    for _ in range(8):
        B = BN_insert(B, 8)
        
    C = BN_add(A, B)
    
    BN_print(C)
