# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Solution 1
        # if head is None:
        #     return None
        
        # length = 0
        # curr = head
        # while curr:
        #     length += 1
        #     curr = curr.next
        
        # mid = length//2
        # pos = 0
        # curr = head
        # while curr:
        #     if pos == mid:
        #         return curr
        #     pos += 1
        #     curr = curr.next


        # Solution 2
        # if head is None:
        #     return None
        
        # slow, fast = head, head
        # while fast:
        #     if fast is None or fast.next is None:
        #         break
        #     else:
        #         fast = fast.next.next
        #     slow = slow.next
        # return slow
        

        # Solution 3
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        return nodes[len(nodes)//2]