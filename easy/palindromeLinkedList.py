class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Solution 1
        # if head is None:
        #     return True
        
        # curr = head
        # stack = []
        
        # while curr:
        #     stack.append(curr)
        #     curr = curr.next
        
        # while head:
        #     ptr = stack.pop()
        #     if head.val != ptr.val:
        #         return False
        #     head = head.next
        # return True

        # Solution 2
        slow, fast, prev = head, head, None

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        prev, slow, prev.next = slow, slow.next, None

        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        
        fast, slow = head, prev

        while slow:
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next
        
        return True