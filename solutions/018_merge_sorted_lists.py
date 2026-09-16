"""
LeetCode 21: Merge Two Sorted Lists
Difficulty: Easy
Topics: Linked List, Recursion

Problem:
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both l1 and l2 are sorted in non-decreasing order.

Approach:
Use a dummy head to simplify edge cases.
Compare nodes from both lists and attach the smaller one to the result.
Move forward in the list from which we took the node.
Continue until one list is exhausted, then attach the remaining nodes.

Time Complexity: O(m + n) where m and n are the lengths of the two lists
Space Complexity: O(1) - Constant extra space (not counting output)
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists.
        
        Args:
            l1: First sorted linked list
            l2: Second sorted linked list
            
        Returns:
            Merged sorted linked list
        """
        # Dummy head to simplify edge cases
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Attach the remaining nodes
        current.next = l1 if l1 else l2
        
        return dummy.next

# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values."""
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    """Convert a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(l1, l2)
    print(f"Test 1: l1 = [1,2,4], l2 = [1,3,4]")
    print(f"Result: {linked_list_to_list(result)}")  # Expected: [1,1,2,3,4,4]
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4]
    
    # Test case 2
    l1 = create_linked_list([])
    l2 = create_linked_list([])
    result = solution.mergeTwoLists(l1, l2)
    print(f"\nTest 2: l1 = [], l2 = []")
    print(f"Result: {linked_list_to_list(result)}")  # Expected: []
    assert linked_list_to_list(result) == []
    
    # Test case 3
    l1 = create_linked_list([])
    l2 = create_linked_list([0])
    result = solution.mergeTwoLists(l1, l2)
    print(f"\nTest 3: l1 = [], l2 = [0]")
    print(f"Result: {linked_list_to_list(result)}")  # Expected: [0]
    assert linked_list_to_list(result) == [0]
    
    # Additional test cases
    l1 = create_linked_list([1, 2, 3])
    l2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(l1, l2)
    print(f"\nTest 4: l1 = [1,2,3], l2 = [4,5,6]")
    print(f"Result: {linked_list_to_list(result)}")  # Expected: [1,2,3,4,5,6]
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6]
    
    l1 = create_linked_list([1, 3, 5, 7])
    l2 = create_linked_list([2, 4, 6, 8])
    result = solution.mergeTwoLists(l1, l2)
    print(f"\nTest 5: l1 = [1,3,5,7], l2 = [2,4,6,8]")
    print(f"Result: {linked_list_to_list(result)}")  # Expected: [1,2,3,4,5,6,7,8]
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6, 7, 8]
    
    l1 = create_linked_list([-10, -5, 0, 5])
    l2 = create_linked_list([-8, -3, 2, 7])
    result = solution.mergeTwoLists(l1, l2)
    print(f"\nTest 6: l1 = [-10,-5,0,5], l2 = [-8,-3,2,7]")
    print(f"Result: {linked_list_to_list(result)}")  # Expected: [-10,-8,-5,-3,0,2,5,7]
    assert linked_list_to_list(result) == [-10, -8, -5, -3, 0, 2, 5, 7]
    
    print("\nAll tests passed!")