# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        current = dummy
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 is not None else list2
        return dummy.next

# Helper: Convert Python list to Linked List
def list_to_linked(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper: Convert Linked List to Python list
def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Driver code
sol = Solution()
l1 = list_to_linked([1, 2, 3, 4])
l2 = list_to_linked([1, 2, 3])
merged_head = sol.mergeTwoLists(l1, l2)
print(linked_to_list(merged_head))  # Output: [1, 1, 2, 2, 3, 3, 4]
