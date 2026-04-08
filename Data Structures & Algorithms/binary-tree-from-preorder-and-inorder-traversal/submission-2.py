# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
            
        root = TreeNode(preorder[0], None, None)

        left_side_preorder, left_side_inorder = [], []
        right_side_preorder, right_side_inorder = [], []
        mid = inorder.index(preorder[0])

        left_side_inorder = inorder[0:mid]
        right_side_inorder = inorder[mid+1:len(inorder)]

        left_side_preorder = preorder[1:len(left_side_inorder)+1]
        right_side_preorder = preorder[len(left_side_inorder)+1:len(preorder)]

        root.left = self.buildTree(left_side_preorder, left_side_inorder)
        root.right = self.buildTree(right_side_preorder, right_side_inorder)
        return root
