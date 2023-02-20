class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head: ListNode):
        prev, curr, nextPtr = None, head, None

        while curr:
            nextPtr = curr.next
            curr.next = prev
            prev = curr
            curr = nextPtr
        
        return prev

    def isPalindrome(self, head: ListNode) -> bool:
        headRev = self.reverse(head)

        curr, currRev = head, headRev

        while curr:
            if curr.val != currRev.val:
                return False
            curr = curr.next
            currRev = currRev.next
        
        return True