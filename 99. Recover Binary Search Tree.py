class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 題目有說只有兩個node錯誤，所以先用中序遍歷來找出錯的 (BST的inorder可由小到大排序)
        def Inorder(node):
            if not node:  # 若為空
                return []
            return Inorder(node.left) + [node] + Inorder(node.right)
        
        # 中序去遍歷
        nodes = Inorder(root)
        
        # 標記是否更新過
        first = None
        Second = None

        # 找出兩個錯誤的節點
        for i in range(len(nodes) - 1):
            if(nodes[i].val > nodes[i+1].val):
                if not first:  # 確保正確標記第一個錯誤，避免重複更新
                    first = nodes[i]
                Second = nodes[i+1]

        first.val, Second.val = Second.val, first.val 
