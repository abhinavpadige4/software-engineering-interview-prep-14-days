"""
LeetCode 27: Remove Element
Difficulty: Easy
Topics: Array, Two Pointers

Problem:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array 
in-place with O(1) extra memory.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_ _]
Explanation: Your function should return k = 2, with the first two elements of nums being 2 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_ _ _ _]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 4, 0, and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
- 0 <= nums.length <= 100
- 0 <= val <= 100
- 0 <= nums[i] <= 100

Approach:
Use two pointers: slow and fast.
Slow pointer tracks the position where next non-val element should go.
Fast pointer scans through the array.
When we find an element not equal to val, we place it at the slow pointer position.

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) - Constant extra space
"""

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    """
    Remove all occurrences of val in nums in-place.
    
    Args:
        nums: List of integers (modified in-place)
        val: Value to remove
        
    Returns:
        Number of elements not equal to val (k)
    """
    # Slow pointer tracks position for next non-val element
    slow = 0
    
    # Fast pointer scans through the array
    for fast in range(len(nums)):
        # When we find an element not equal to val
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    
    # Return count of elements not equal to val
    return slow

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = removeElement(nums1, val1)
    print(f"Test 1: nums = [3,2,2,3], val = {val1}")
    print(f"Result: k = {k1}, nums = {nums1}")  # Expected: k = 2, nums = [2,2,_ _]
    assert k1 == 2
    assert sorted(nums1[:k1]) == [2, 2]  # Order may vary
    
    # Test case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = removeElement(nums2, val2)
    print(f"\nTest 2: nums = [0,1,2,2,3,0,4,2], val = {val2}")
    print(f"Result: k = {k2}, nums = {nums2}")  # Expected: k = 5, nums = [0,1,4,0,3,_ _ _ _]
    assert k2 == 5
    assert sorted(nums2[:k2]) == [0, 0, 1, 3, 4]  # Order may vary
    
    # Test case 3
    nums3 = [3, 3, 3, 3]
    val3 = 3
    k3 = removeElement(nums3, val3)
    print(f"\nTest 3: nums = [3,3,3,3], val = {val3}")
    print(f"Result: k = {k3}, nums = {nums3}")  # Expected: k = 0, nums = [_ _ _ _]
    assert k3 == 0
    assert nums3[:k3] == []
    
    # Test case 4
    nums4 = [0, 1, 2, 3, 4, 5]
    val4 = 6  # Value not in array
    k4 = removeElement(nums4, val4)
    print(f"\nTest 4: nums = [0,1,2,3,4,5], val = {val4}")
    print(f"Result: k = {k4}, nums = {nums4}")  # Expected: k = 6, nums = [0,1,2,3,4,5]
    assert k4 == 6
    assert nums4[:k4] == [0, 1, 2, 3, 4, 5]
    
    # Test case 5
    nums5 = []
    val5 = 5
    k5 = removeElement(nums5, val5)
    print(f"\nTest 5: nums = [], val = {val5}")
    print(f"Result: k = {k5}, nums = {nums5}")  # Expected: k = 0, nums = []
    assert k5 == 0
    assert nums5[:k5] == []
    
    # Test case 6
    nums6 = [1]
    val6 = 1
    k6 = removeElement(nums6, val6)
    print(f"\nTest 6: nums = [1], val = {val6}")
    print(f"Result: k = {k6}, nums = {nums6}")  # Expected: k = 0, nums = [_]
    assert k6 == 0
    assert nums6[:k6] == []
    
    # Test case 7
    nums7 = [1]
    val7 = 2  # Value not in array
    k7 = removeElement(nums7, val7)
    print(f"\nTest 7: nums = [1], val = {val7}")
    print(f"Result: k = {k7}, nums = {nums7}")  # Expected: k = 1, nums = [1]
    assert k7 == 1
    assert nums7[:k7] == [1]
    
    print("\nAll tests passed!")