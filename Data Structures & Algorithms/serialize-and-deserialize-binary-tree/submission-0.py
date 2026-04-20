import ast

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "[]"

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            level_vals = []

            for _ in range(level_size):
                cur = queue.popleft()

                if cur:
                    level_vals.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    level_vals.append(None)

            if level_vals:
                result.append(level_vals)

        return str(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree_lists = ast.literal_eval(data)

        if not tree_lists:
            return None

        root = TreeNode(tree_lists[0][0])
        queue = deque([root])

        level_index = 1

        while queue and level_index < len(tree_lists):
            level_vals = tree_lists[level_index]
            i = 0
            next_queue = deque()

            while queue and i < len(level_vals):
                node = queue.popleft()

                if i < len(level_vals) and level_vals[i] is not None:
                    node.left = TreeNode(level_vals[i])
                    next_queue.append(node.left)
                i += 1

                if i < len(level_vals) and level_vals[i] is not None:
                    node.right = TreeNode(level_vals[i])
                    next_queue.append(node.right)
                i += 1

            queue = next_queue
            level_index += 1

        return root
