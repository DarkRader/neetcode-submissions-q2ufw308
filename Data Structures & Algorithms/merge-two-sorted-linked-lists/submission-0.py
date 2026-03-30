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

        res = []

        while list1 and list2:
            if list1.val > list2.val:
                res.append(list2.val)
                list2 = list2.next
            else:
                res.append(list1.val)
                list1 = list1.next

        left_list = None
        if list1:
            left_list = list1
        else:
            left_list = list2

        while left_list:
            res.append(left_list.val)
            left_list = left_list.next

        res_list = ListNode()
        new_sorted_list = res_list
        i = 0
        while i < len(res):
            new_sorted_list.val = res[i]
            if i != len(res) - 1:
                new_sorted_list.next = ListNode()
                new_sorted_list = new_sorted_list.next
            i += 1

        return res_list
