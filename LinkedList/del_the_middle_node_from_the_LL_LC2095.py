# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        fast = head
        n = count // 2
        for i in range(n-1):
            fast = fast.next
        fast.next = fast.next.next
        return head
