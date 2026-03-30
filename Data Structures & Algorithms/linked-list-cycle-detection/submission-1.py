# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        map_dict = {}

        counter = 0
        while head:
            map_dict[head] = 1 + map_dict.get(head, 0)
            if map_dict[head] > 1:
                return True
            head = head.next
            counter += 1

        return False
        