# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        t = head
        l = []
        while t:
            l.append(t.val)
            t = t.next
        k = k % len(l)
        if k == 0:
            return head
        ll = l[-k:] + l[:-k]
        dummy = ListNode(0)
        curr = dummy
        for val in ll:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next