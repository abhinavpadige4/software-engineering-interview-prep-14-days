"""
LeetCode 24: Swap Nodes in Pairs
Difficulty: Medium
Topics: Linked List, Recursion

Problem:
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Example 4:
Input: head = [1,2,3]
Output: [2,1,3]

Constraints:
- The number of nodes in the list is in the range [0, 100].
- 0 <= Node.val <= 100

Approach:
Use a dummy head to simplify edge cases.
Swap pairs by adjusting pointers:
1. Point previous node to second node
2. Point second node to first node  
3. Point first node to what second node was pointing to
4. Move previous pointer to first node for next iteration

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(1) - Constant extra space
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swap every two adjacent nodes in a linked list.
        
        Args:
            head: Head of the linked list
            
        Returns:
            Head of the modified linked list with pairs swapped
        """
        # Dummy head to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # While there are at least two nodes left to swap
        while prev.next and prev.next.next:
            # Identify the two nodes to swap
            first = prev.next
            second = prev.next.next
            
            # Perform the swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move prev to the first node for next pair
            prev = first
        
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
    head1 = create_linked_list([1, 2, 3, 4])
    result1 = solution.swapPairs(head1)
    print(f"Test 1: head = [1,2,3,4]")
    print(f"Result: {linked_list_to_list(result1)}")  # Expected: [2,1,4,3]
    assert linked_list_to_list(result1) == [2, 1, 4, 3]
    
    # Test case 2
    head2 = create_linked_list([])
    result2 = solution.swapPairs(head2)
    print(f"\nTest 2: head = []")
    print(f"Result: {linked_list_to_list(result2)}")  # Expected: []
    assert linked_list_to_list(result2) == []
    
    # Test case 3
    head3 = create_linked_list([1])
    result3 = solution.swapPairs(head3)
    print(f"\nTest 3: head = [1]")
    print(f"Result: {linked_list_to_list(result3)}")  # Expected: [1]
    assert linked_list_to_list(result3) == [1]
    
    # Test case 4
    head4 = create_linked_list([1, 2, 3])
    result4 = solution.swapPairs(head4)
    print(f"\nTest 4: head = [1,2,3]")
    print(f"Result: {linked_list_to_list(result4)}")  # Expected: [2,1,3]
    assert linked_list_to_list(result4) == [2, 1, 3]
    
    # Additional test cases
    head5 = create_linked_list([1, 2, 3, 4, 5])
    result5 = solution.swapPairs(head5)
    print(f"\nTest 5: head = [1,2,3,4,5]")
    print(f"Result: {linked_list_to_list(result5)}")  # Expected: [2,1,4,3,5]
    assert linked_list_to_list(result5) == [2, 1, 4, 3, 5]
    
    head6 = create_linked_list([1, 2, 3, 4, 5, 6])
    result6 = solution.swapPairs(head6)
    print(f"\nTest 6: head = [1,2,3,4,5,6]")
    print(f"Result: {linked_list_to_list(result6)}")  # Expected: [2,1,4,3,6,5]
    assert linked_list_to_list(result6) == [2, 1, 4, 3, 6, 5]
    
    head7 = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    result7 = solution.swapPairs(head7)
    print(f"\nTest 7: head = [1,2,3,4,5,6,7]")
    print(f"Result: {linked_list_to_list(result7)}")  # Expected: [2,1,4,3,6,5,7]
    assert linked_list_to_list(result7) == [2, 1, 4, 3, 6, 5, 7]
    
    print("\nAll tests passed!")