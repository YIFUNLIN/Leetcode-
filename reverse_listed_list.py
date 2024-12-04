# Leetcode 206. Reverse Linked List

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev
