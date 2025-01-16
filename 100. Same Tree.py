class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
            
        # 檢查檢點是否相同&左右子樹
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
