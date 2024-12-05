# Leetcode: 9. Palindrome Number
# 法一: 利用stack 作法
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:   # 負數不可能回文
            return False

        num_str = str(x)  # 先轉成字串，方便後續處理
        stack = []  # 利用stack 特性來處理
        mid = len(num_str) // 2  # 先抓出中間值

        # 若是奇數，直接跳過中間那個
        if len(num_str) % 2 == 1:
            mid += 1

        # 先將左半部壓入stack中
        for i in range(0,mid):
            stack.append(num_str[i])
        
        for j in range(mid,len(num_str)): # 遍歷右半部分
            if num_str[j] == stack[-1]:  # 將迴圈指到的值與stack 的頂端值做比較
                stack.pop()    # 相同就取出stack top 值
            else:
                return False   # 任一個不同就回傳False
        return True
        

# 法二
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the number to a string
        num_str = str(x)
        # Check if the string is equal to its reverse
        return num_str == num_str[::-1]


# 法三: 逐位提取數字並重建倒序數   詳細解釋: https://hackmd.io/@Linnn/H1jUPPNmyl
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_num = 0
        original = x

        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return x == reversed_num or x == reversed_num // 10


