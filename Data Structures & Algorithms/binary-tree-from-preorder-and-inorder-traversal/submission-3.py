# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.preorder_idx = 0

        def dfs(in_left, in_right):
            if in_left > in_right:
                return None

            root_val = preorder[self.preorder_idx]
            root = TreeNode(root_val)
            self.preorder_idx += 1

            mid = inorder_map[root_val]
            root.left = dfs(in_left, mid - 1)
            root.right = dfs(mid + 1, in_right)
            
            return root

        return dfs(0, len(inorder) - 1)