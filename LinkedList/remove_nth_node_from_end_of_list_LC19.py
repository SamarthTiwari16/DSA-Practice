# Optimal TC=O(N) SC=O(1)  In ONE pass

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        if count == n:
            return head.next
        m = count - n
        fast = head
        for i in range(m-1):
            fast = fast.next
        fast.next = fast.next.next
        return head
