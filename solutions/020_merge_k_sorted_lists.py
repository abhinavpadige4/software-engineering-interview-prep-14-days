"""
LeetCode 23: Merge k Sorted Lists
Difficulty: Hard
Topics: Linked List, Divide and Conquer, Heap/Priority Queue

Problem:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.

Approach:
Use a min-heap (priority queue) to efficiently get the smallest element.
1. Add the first node of each list to the heap
2. Repeatedly extract the minimum and add its next node to the heap
3. Build the result list by attaching extracted nodes

Time Complexity: O(N log k) where N is total number of nodes, k is number of lists
Space Complexity: O(k) for the heap
"""

from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Define comparison method for ListNode to work with heapq
ListNode.__lt__ = lambda self, other: self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into one sorted list.
        
        Args:
            lists: Array of linked list heads
            
        Returns:
            Head of the merged sorted linked list
        """
        # Handle edge cases
        if not lists or all(l is None for l in lists):
            return None
        
        # Min-heap to store (value, list_index, node) tuples
        # We use list_index to avoid comparison issues when values are equal
        heap = []
        
        # Add the first node of each list to the heap
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        # Dummy head for the result list
        dummy = ListNode(0)
        current = dummy
        
        # Extract min from heap and add next node from same list
        while heap:
            val, list_idx, node = heapq.heappop(heap)
            
            # Add the smallest node to result
            current.next = node
            current = current.next
            
            # If there's a next node in the same list, add it to heap
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
        
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
    lists1 = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    result1 = solution.mergeKLists(lists1)
    print(f"Test 1: lists = [[1,4,5],[1,3,4],[2,6]]")
    print(f"Result: {linked_list_to_list(result1)}")  # Expected: [1,1,2,3,4,4,5,6]
    assert linked_list_to_list(result1) == [1, 1, 2, 3, 4, 4, 5, 6]
    
    # Test case 2
    lists2 = []
    result2 = solution.mergeKLists(lists2)
    print(f"\nTest 2: lists = []")
    print(f"Result: {linked_list_to_list(result2)}")  # Expected: []
    assert linked_list_to_list(result2) == []
    
    # Test case 3
    lists3 = [create_linked_list([])]
    result3 = solution.mergeKLists(lists3)
    print(f"\nTest 3: lists = [[]]")
    print(f"Result: {linked_list_to_list(result3)}")  # Expected: []
    assert linked_list_to_list(result3) == []
    
    # Additional test cases
    lists4 = [
        create_linked_list([]),
        create_linked_list([1]),
        create_linked_list([2, 3])
    ]
    result4 = solution.mergeKLists(lists4)
    print(f"\nTest 4: lists = [[],[1],[2,3]]")
    print(f"Result: {linked_list_to_list(result4)}")  # Expected: [1,2,3]
    assert linked_list_to_list(result4) == [1, 2, 3]
    
    lists5 = [
        create_linked_list([1, 2, 3]),
        create_linked_list([4, 5, 6]),
        create_linked_list([7, 8, 9])
    ]
    result5 = solution.mergeKLists(lists5)
    print(f"\nTest 5: lists = [[1,2,3],[4,5,6],[7,8,9]]")
    print(f"Result: {linked_list_to_list(result5)}")  # Expected: [1,2,3,4,5,6,7,8,9]
    assert linked_list_to_list(result5) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    lists6 = [
        create_linked_list([1, 3, 5]),
        create_linked_list([2, 4, 6])
    ]
    result6 = solution.mergeKLists(lists6)
    print(f"\nTest 6: lists = [[1,3,5],[2,4,6]]")
    print(f"Result: {linked_list_to_list(result6)}")  # Expected: [1,2,3,4,5,6]
    assert linked_list_to_list(result6) == [1, 2, 3, 4, 5, 6]
    
    print("\nAll tests passed!")