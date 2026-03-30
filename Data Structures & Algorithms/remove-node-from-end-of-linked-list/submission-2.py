# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n == 1:
            return None

        count = 0
        new_head = head 
        while new_head != None:
            count += 1
            new_head = new_head.next

        node_for_del = count - n + 1
        if node_for_del == 1:
            return head.next

        print(node_for_del)
        count = 0
        new_head = head 
        while new_head != None:
            count += 1
            if count + 1 == node_for_del:
                new_head.next = new_head.next.next
                break
            new_head = new_head.next
            
       
        return head
        