# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Initialize a dummy node and a current pointer
        dummy = ListNode()
        current = dummy
        
        # 2. Traverse both lists while neither is empty
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1  # Attach list1's node
                list1 = list1.next    # Move list1 forward
            else:
                current.next = list2  # Attach list2's node
                list2 = list2.next    # Move list2 forward
            
            # Move our current pointer forward to the new tail
            current = current.next
            
        # 3. Attach any remaining nodes from either list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
            
        # 4. Return the actual head of the merged list (skipping the dummy)
        return dummy.next