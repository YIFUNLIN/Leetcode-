# Leetcode: 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s: 
            if c in '([{':   # 如果當前字符 c 是左括號（(, [, {），則將其壓入堆疊
                stack.append(c)
            else:                  # 如果堆疊為空或找不到對應的括號，直接返回 False
                if not stack or \
                    (c == ")" and stack[-1] != '(') or \
                    (c == "]" and stack[-1] != "[") or \
                    (c == "}" and stack[-1] != "{"):
                    return False
                stack.pop()   # 有找到就pop
        return not stack # 最後檢查堆疊是否為空，(stack為空:False)、(stack有值:True) => True ，表示所有括號均成功匹配，返回 True 反之False
