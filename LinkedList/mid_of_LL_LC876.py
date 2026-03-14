# TC=O(logN) SC=O(1)
head = [1,2,3,4,5]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mid_of_LL(head):
    slow = head
    fast = head
    while fast and fast.next:  # when both are not None
        slow = slow.next
        fast = fast.next.next
    return slow
print(mid_of_LL(head))
