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
