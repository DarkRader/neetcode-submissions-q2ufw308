# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, left_border, right_border):
            if not node:
                return True

            if not (left_border < node.val < right_border):
                return False

            left, right = dfs(node.left, left_border, node.val), dfs(node.right, node.val, right_border)
            return left and right

        return dfs(root, float('-inf'), float('inf'))
