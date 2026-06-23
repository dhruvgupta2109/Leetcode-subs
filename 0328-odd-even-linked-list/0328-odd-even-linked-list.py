# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return 
        o_dummy = ListNode(0)
        e_dummy = ListNode(0)
        o = o_dummy
        e = e_dummy
        curr = head
        i = 1
        while curr:
            if i % 2 != 0:
                o.next = curr
                o = o.next
            else:
                e.next = curr
                e = e.next
            curr = curr.next
            i += 1
        e.next = None
        o.next = e_dummy.next
        return o_dummy.next