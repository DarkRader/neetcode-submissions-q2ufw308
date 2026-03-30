# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        tmp_elem = None
        new_list = ListNode()
        head = new_list
        while list1 and list2:
            if list1.val > list2.val:
                new_list.val = list2.val
                list2 = list2.next
            else: 
                new_list.val = list1.val
                list1 = list1.next
            new_list.next = ListNode()
            new_list = new_list.next

        left_list = None
        if list1:
            left_list = list1
        else:
            left_list = list2

        while left_list:
            new_list.val = left_list.val
            left_list = left_list.next
            if left_list:
                new_list.next = ListNode()
                new_list = new_list.next

        return head
