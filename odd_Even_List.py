# 328. Odd Even Linked List

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None:
            odd_head = head   # 先建立奇數節點
            odd_node = odd_head
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
                odd_node = odd_node.next # 往右走一格
            else: # 若當前節點是偶數
                even_node.next = head
                even_node = even_node.next
            head = head.next # head 移動到下個node
            count += 1
        
        odd_node.next = even_head # 將偶節點的串列 連接至奇數節點最後
        even_node.next = None
        return odd_head
