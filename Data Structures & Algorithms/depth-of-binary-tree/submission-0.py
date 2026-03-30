# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_sub_tree = self.maxDepth(root.left)
        right_sub_tree = self.maxDepth(root.right)

        sum_depth = max(left_sub_tree, right_sub_tree) + 1

        return sum_depth
        