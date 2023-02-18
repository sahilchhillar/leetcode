class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElementFromLinkedList(head: ListNode, val):
    if head is None:
        return head

    while head:
        if head.val != val:
            break
        head = head.next
        
    curr = head

    while curr:
        nextPtr = curr.next
        while nextPtr and nextPtr.val == val:
            nextPtr = nextPtr.next
        curr.next = nextPtr
        curr = curr.next
        
    return head