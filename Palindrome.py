# Leetcode: 9. Palindrome Number
# 法一
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the number to a string
        num_str = str(x)
        # Check if the string is equal to its reverse
        return num_str == num_str[::-1]


# 法二: 逐位提取數字並重建倒序數   詳細解釋: https://hackmd.io/@Linnn/H1jUPPNmyl
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

# 法三: 使用stack
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # 負數不可能回文
            return False
        # Convert the number to a string
        num_str = str(x)
        stack = []

        # 將前半部分壓入stack中
        mid = len(num_str) // 2
        for i in range(mid):
            stack.append(num_str[i])

        # 若是奇數，略過中間字符
        if len(num_str) % 2 != 0:
            mid += 1
        # 從stack 中一一 pop 掉以跟後面做比較
        for i in range(mid,len(num_str)):
            if(stack.pop() != num_str[i]):
                return False
        return True

