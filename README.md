# Leetcode
### 刷題格式須知
```
class Solution:
    def findGCD(self, nums: List[int]) -> int:
```
等同於
```
class Solution:
    def findGCD(self, nums):
```

1. findGCD: 這是函式的名稱。在這個例子中，這個名稱暗示這個函式可能用於找出一組數字的最大公約數（GCD，Greatest Common Divisor）。

2. (self, nums: List[int]): 這是函式的參數列表。
    - self：這個參數表明這個函式可能是一個類別（class）的方法。在類別的方法中，self 參數代表了類別的實例本身。
    - nums: List[int]：這表明函式接受一個參數 nums，它是一個由整數（int）組成的列表（List）。這裡的 List[int] 是 Python 的類型註解（type hint），用於說明 nums 應該是一個整數列表。
    - -> int: 這是一個返回類型註解，指出這個函式返回一個整數（int）。這意味著函式的目的是從它處理的數據中計算出一個整數值，並將這個值返回給調用者。

---

437. Path Sum III [Medium]

> https://leetcode.com/problems/path-sum-iii/?envType=study-plan-v2&envId=leetcode-75

> Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
> 
> The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

> ### 題目描述：
> 這道題目（Path Sum III）是給你一個二元樹的根節點和一個整數 targetSum，要你返回二元樹中有多少條路徑的節點值之和等於 targetSum。這裡的路徑不必從根節點開始，也不必在葉子節點結束，但必須是向下的路徑（即只能從父節點走到子節點）。

![](https://hackmd.io/_uploads/HJ7Uw6xM6.png =60%x)
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, target, prefix_sum, prefix_sums): #prefix_sum:根節點到當前節點的路徑所有節點值總和
                                                    # 而prefix_sum 是一個字典，來記錄重複的次數與走過的node
            if node is None:  # 若當前節點為空，代表已經到了底部
                return 0

            prefix_sum += node.val # 將當前node的值與prefix_sum 相加，也就是跟之前走過的node做加總
            count = prefix_sums.get(prefix_sum - target, 0) # 剩下的和是否已經在我之前的路徑中看到過。如果我之前看到過，那麼從那個點到我現在的位置形成的路徑，其和就是目標值

            prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1

            count += dfs(node.left, target, prefix_sum, prefix_sums) + dfs(node.right, target, prefix_sum, prefix_sums)   # 利用Recrusive 往左右子樹去找

            prefix_sums[prefix_sum] -= 1

            return count

        prefix_sums = {0: 1}  # Initialize with a prefix sum of 0
        return dfs(root, targetSum, 0, prefix_sums)

```

[概念]
1. prefix_sum 是用來記錄從root走到當前路徑(第一條會從10->5->3->3走)的所有節點總和
2. prefix_sums 在下面的程式碼把它定義成一個字典，用來記錄累積次數與走過的node
3. prefix_sum每次都會跟當前走到的新node做加總
4. 再利用 prefix_sum -target ，得出的值若與之前走過的node的值有相同的出， 則代表該路徑是存在的，累積+1
5. 就一直recrusive，左右子樹，到了Leaf走不下去，在退一步回去
![](https://hackmd.io/_uploads/S1i25alf6.png)


### LCS(Longest Common Subsequence)
> https://leetcode.com/problems/longest-common-subsequence/description/

> Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.


![S__3342414](https://hackmd.io/_uploads/rJO_kLaD6.jpg)



```
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:  # 提示用
        m = len(text1)
        n = len(text2)
        c = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    c[i][j] = 1 + c[i-1][j-1]
                else:
                    c[i][j] = max(c[i-1][j],c[i][j-1])
        return c[m][n]
    
    #####################     End      #########################
## Test 
text1 = "abcde"
text2 = "ace"

# 創建 Solution 類別的實例
solution = Solution()

# 使用實例來呼叫 longestCommonSubsequence 方法
print(solution.longestCommonSubsequence(text1, text2))
```
