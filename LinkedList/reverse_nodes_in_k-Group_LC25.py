# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        temp = head
        prev = None

        length = 0
        while temp:
            length += 1
            temp = temp.next

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        temp = head
        while length >= k:
            group_start = temp
            prev = None
            for i in range(k):
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
            prev_group_end.next = prev
            group_start.next = temp
            prev_group_end = group_start
            length -= k
        return dummy.next
