"""
LeetCode 25: Reverse Nodes in k-Group
Difficulty: Hard
Topics: Linked List, Recursion

Problem:
Given the head of a linked list, reverse the nodes of the list k at a time, 
and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, 
should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 3:
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 4:
Input: head = [1,2,3,4,5], k = 5
Output: [5,4,3,2,1]

Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

Approach:
Use recursion or iterative approach:
1. Check if there are at least k nodes left to reverse
2. If yes, reverse those k nodes
3. Recursively process the rest of the list
4. Connect the reversed part with the processed rest

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(1) for iterative, O(n/k) for recursive (call stack)
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse nodes of the list k at a time.
        
        Args:
            head: Head of the linked list
            k: Group size for reversal
            
        Returns:
            Head of the modified linked list
        """
        # Helper function to reverse a linked list
        def reverse_linked_list(start, end):
            """
            Reverse the linked list from start to end (exclusive).
            
            Args:
                start: Starting node
                end: Ending node (exclusive)
                
            Returns:
                Tuple of (new_head, new_tail) of reversed segment
            """
            prev = None
            current = start
            while current != end:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev, start  # new_head, new_tail
        
        # Dummy head to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy  # Node before the current group
        
        while True:
            # Check if there are at least k nodes left
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # Not enough nodes left, return result
            
            # Group to reverse: group_prev.next to kth
            group_next = kth.next  # Node after the kth node
            
            # Reverse the group
            new_head, new_tail = reverse_linked_list(group_prev.next, group_next)
            
            # Reconnect the reversed group
            group_prev.next = new_head
            new_tail.next = group_next
            
            # Move group_prev to the end of the reversed group
            group_prev = new_tail
    
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
    k1 = 2
    result1 = solution.reverseKGroup(head1, k1)
    print(f"Test 1: head = [1,2,3,4,5], k = {k1}")
    print(f"Result: {linked_list_to_list(result1)}")  # Expected: [2,1,4,3,5]
    assert linked_list_to_list(result1) == [2, 1, 4, 3, 5]
    
    # Test case 2
    head2 = create_linked_list([1, 2, 3, 4, 5])
    k2 = 3
    result2 = solution.reverseKGroup(head2, k2)
    print(f"\nTest 2: head = [1,2,3,4,5], k = {k2}")
    print(f"Result: {linked_list_to_list(result2)}")  # Expected: [3,2,1,4,5]
    assert linked_list_to_list(result2) == [3, 2, 1, 4, 5]
    
    # Test case 3
    head3 = create_linked_list([1, 2, 3, 4, 5])
    k3 = 1
    result3 = solution.reverseKGroup(head3, k3)
    print(f"\nTest 3: head = [1,2,3,4,5], k = {k3}")
    print(f"Result: {linked_list_to_list(result3)}")  # Expected: [1,2,3,4,5]
    assert linked_list_to_list(result3) == [1, 2, 3, 4, 5]
    
    # Test case 4
    head4 = create_linked_list([1, 2, 3, 4, 5])
    k4 = 5
    result4 = solution.reverseKGroup(head4, k4)
    print(f"\nTest 4: head = [1,2,3,4,5], k = {k4}")
    print(f"Result: {linked_list_to_list(result4)}")  # Expected: [5,4,3,2,1]
    assert linked_list_to_list(result4) == [5, 4, 3, 2, 1]
    
    # Additional test cases
    head5 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    k5 = 3
    result5 = solution.reverseKGroup(head5, k5)
    print(f"\nTest 5: head = [1,2,3,4,5,6,7,8], k = {k5}")
    print(f"Result: {linked_list_to_list(result5)}")  # Expected: [3,2,1,6,5,4,7,8]
    assert linked_list_to_list(result5) == [3, 2, 1, 6, 5, 4, 7, 8]
    
    head6 = create_linked_list([1, 2, 3, 4])
    k6 = 4
    result6 = solution.reverseKGroup(head6, k6)
    print(f"\nTest 6: head = [1,2,3,4], k = {k6}")
    print(f"Result: {linked_list_to_list(result6)}")  # Expected: [4,3,2,1]
    assert linked_list_to_list(result6) == [4, 3, 2, 1]
    
    head7 = create_linked_list([1, 2, 3])
    k7 = 2
    result7 = solution.reverseKGroup(head7, k7)
    print(f"\nTest 7: head = [1,2,3], k = {k7}")
    print(f"Result: {linked_list_to_list(result7)}")  # Expected: [2,1,3]
    assert linked_list_to_list(result7) == [2, 1, 3]
    
    print("\nAll tests passed!")