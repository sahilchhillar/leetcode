class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head: ListNode):
    if head is None:
        return head
    
    prev, curr, nextPtr = None, head, None
    while curr:
        nextPtr = curr.next
        curr.next = prev
        prev = curr
        curr = nextPtr
    return prev