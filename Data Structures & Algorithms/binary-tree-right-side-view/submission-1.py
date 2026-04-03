# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        result = []

        while queue:
            right_side = None
            level_size = len(queue)

            for _ in range(level_size):
                curr = queue.popleft()

                if curr:
                    right_side = curr
                    queue.append(curr.left)
                    queue.append(curr.right)

            if right_side:
                result.append(right_side.val)
                
        return result
        