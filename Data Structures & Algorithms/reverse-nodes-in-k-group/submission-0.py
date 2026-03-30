# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_len = 0
        count_head = head
        while count_head:
            count_head = count_head.next
            list_len += 1

        new_head = None
        prev_tail, curr = None, head
        count = list_len

        while count >= k:
            group_head = curr
            prev = None
            temp_k = k
            
            while temp_k > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                temp_k -= 1

            if not new_head:
                new_head = prev
            if prev_tail:
                prev_tail.next = prev

            prev_tail = group_head
            count -= k

        if prev_tail:
            prev_tail.next = curr

        return new_head if new_head else head
