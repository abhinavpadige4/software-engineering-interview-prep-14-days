"""
LeetCode 19: Remove Nth Node From End of List
Difficulty: Medium
Topics: Linked List, Two Pointers

Problem:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 1 <= n <= sz

Approach:
Use two pointers with a gap of n nodes between them.
Move both pointers together until the front pointer reaches the end.
The back pointer will then be at the node before the one to be removed.

Time Complexity: O(L) where L is the length of the linked list
Space Complexity: O(1) - Constant extra space
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of the list.
        
        Args:
            head: Head of the linked list
            n: Position from the end to remove (1-indexed)
            
        Returns:
            Head of the modified linked list
        """
        # Create a dummy node to handle edge cases (like removing head)
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers
        first = dummy
        second = dummy
        
        # Move first pointer n+1 steps ahead
        # This creates a gap of n nodes between first and second
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until first reaches the end
        # When first is at the end, second will be at the node before the one to remove
        while first:
            first = first.next
            second = second.next
        
        # Skip the nth node from end
        second.next = second.next.next
        
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
    head1 = create_linked_list([1, 2, 3, 4, 5])
    n1 = 2
    result1 = solution.removeNthFromEnd(head1, n1)
    print(f"Test 1: head = [1,2,3,4,5], n = {n1}")
    print(f"Result: {linked_list_to_list(result1)}")  # Expected: [1,2,3,5]
    assert linked_list_to_list(result1) == [1, 2, 3, 5]
    
    # Test case 2
    head2 = create_linked_list([1])
    n2 = 1
    result2 = solution.removeNthFromEnd(head2, n2)
    print(f"\nTest 2: head = [1], n = {n2}")
    print(f"Result: {linked_list_to_list(result2)}")  # Expected: []
    assert linked_list_to_list(result2) == []
    
    # Test case 3
    head3 = create_linked_list([1, 2])
    n3 = 1
    result3 = solution.removeNthFromEnd(head3, n3)
    print(f"\nTest 3: head = [1,2], n = {n3}")
    print(f"Result: {linked_list_to_list(result3)}")  # Expected: [1]
    assert linked_list_to_list(result3) == [1]
    
    # Additional test cases
    head4 = create_linked_list([1, 2, 3, 4, 5])
    n4 = 5  # Remove first node
    result4 = solution.removeNthFromEnd(head4, n4)
    print(f"\nTest 4: head = [1,2,3,4,5], n = {n4} (remove first)")
    print(f"Result: {linked_list_to_list(result4)}")  # Expected: [2,3,4,5]
    assert linked_list_to_list(result4) == [2, 3, 4, 5]
    
    head5 = create_linked_list([1, 2, 3, 4, 5])
    n5 = 1  # Remove last node
    result5 = solution.removeNthFromEnd(head5, n5)
    print(f"\nTest 5: head = [1,2,3,4,5], n = {n5} (remove last)")
    print(f"Result: {linked_list_to_list(result5)}")  # Expected: [1,2,3,4]
    assert linked_list_to_list(result5) == [1, 2, 3, 4]
    
    print("\nAll tests passed!")