# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
            
        curr = head
        nextPtr = curr.next
        while nextPtr:
            if curr.val == nextPtr.val:
                nextPtr = nextPtr.next
                curr.next = nextPtr
            else:
                nextPtr = nextPtr.next
                curr = curr.next
        return head
        