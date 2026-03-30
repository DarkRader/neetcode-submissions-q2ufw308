# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        if leftDepth == -1 or rightDepth == -1:
            return False

        print(leftDepth)
        print(rightDepth)
        maxDepth = max(leftDepth, rightDepth)
        minDepth = min(leftDepth, rightDepth)

        if maxDepth == minDepth or maxDepth == minDepth + 1:
            return True
        else:
            return False

        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if left > right + 1 or right > left + 1 or left == -1 or right == -1:
            return -1

        return max(left, right) + 1
