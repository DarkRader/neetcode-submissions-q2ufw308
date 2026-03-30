# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        extra = 0
        while l1 and l2:
            sum_nums = l1.val + l2.val + extra
            if sum_nums < 10:
                extra = 0
                l1.val = sum_nums
            else:
                extra = 1
                l1.val = sum_nums % 10

            print(l1.val)

            if not l1.next and not l2.next:
                if extra == 1:
                    l1.next = ListNode(extra, None)
                return head
            elif l1.next and not l2.next:
                l1 = l1.next
                break
            elif l2.next and not l1.next:
                l1.next = l2.next
                l1 = l1.next
                break
            else:
                l1, l2 = l1.next, l2.next


        while l1:
            l1_tmp = l1
            sum_nums = l1.val + extra
            if sum_nums < 10:
                l1.val = sum_nums
                extra = 0
            else:
                extra = 1
                l1.val = sum_nums % 10

            l1 = l1.next

            if not l1 and extra == 1:
                l1_tmp.next = ListNode(extra, None)


        return head