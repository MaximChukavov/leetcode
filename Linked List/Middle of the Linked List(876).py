# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        result = []

        while fast and fast.next:
            if fast == None:
                result.append(slow)
            slow = slow.next
            fast = fast.next.next
        return head