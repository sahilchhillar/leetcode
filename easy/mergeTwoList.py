class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoList(list1: ListNode, list2: ListNode):
    if list1 == None:
        return list2
    elif list2 == None:
        return list1
    
    head = list3 = ListNode()

    while list1 and list2:
        if list1.val <= list2.val:
            list3.next = list1
            list1 = list1.next
        else:
            list3.next = list2
            list2 = list2.next
        list3 = list3.next

    if list1:
        list3.next = list1
    elif list2:
        list3.next = list2
    
    return head.next