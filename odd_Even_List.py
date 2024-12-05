# Leetcode: 328. Odd Even Linked List 
# 法一. (個人覺得比較好記)
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:  # 若串列為空，或只有一個節點就直接回傳
            return head
        odd = head   # 作為後續在link list 上找出奇數的node
        even = odd.next
        even_head = even

        while even != None and even.next != None: # 確認偶數串列和偶數節點的下一個都有值才做
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head  # 要將odd的尾端去跟even的頭連接
        return head

# 法二.
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None:
            odd_head = head   # 先建立奇數節點
            odd_node = odd_head # odd_node: 會移動、而odd_head: 代表該串列的頭(不變動)
            head = head.next
        else:
            return None
        
        if head != None:  # 若第二個節點不為空
            even_head = head
            even_node = even_head
            head = head.next
        else:
            return odd_head # 若沒有第二個節點，直接返回odd_head

        count = 3
        while head != None:
            if count % 2 == 1:  # 若當前節點是奇數
                odd_node.next = head # 將當前節點加入奇數鏈表
                odd_node = odd_node.next # 將奇數點移到新指向的節點上
            else: # 若當前節點是偶數
                even_node.next = head
                even_node = even_node.next
            head = head.next # head 移動到下個node
            count += 1
        
        odd_node.next = even_head # 將偶節點的串列頭 連接至奇數節點的最後
        even_node.next = None     # 將偶節點的最後指向None
        return odd_head           # 傳回奇數串列的頭
