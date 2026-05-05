# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Base cases: empty list or single node
        if not head or not head.next or k == 0:
            return head
        
        # 2. Compute the length of the list and find the old tail
        old_tail = head
        length = 1
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
            
        # 3. Connect tail to head to make it circular
        old_tail.next = head
        
        # 4. Find the actual number of rotations needed
        # (k could be larger than the length of the list)
        k = k % length
        
        # If k % length is 0, we are back at the original head
        if k == 0:
            old_tail.next = None
            return head
            
        # 5. Find the new tail: (length - k - 1) steps from the head
        new_tail_steps = length - k - 1
        new_tail = head
        for _ in range(new_tail_steps):
            new_tail = new_tail.next
            
        # 6. Set the new head and break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head