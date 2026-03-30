# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = ListNode(1001, None)
        list_order = -1

        ## Find head:
        for i, l in enumerate(lists):
            if not l:
                continue
            if l.val < head.val:
                head = l
                list_order = i

        lists[list_order] = head.next
        cur_node = head

        counter = 0

        while True:
            min_val = 1001
            for i, l in enumerate(lists):
                if not l:
                    counter += 1
                    continue
                if l.val < min_val:
                    min_val = l.val
                    list_order = i

            if counter == len(lists):
                break

            counter = 0
            cur_node.next = lists[list_order]
            cur_node = cur_node.next
            lists[list_order] = lists[list_order].next

        return head       
            