"""
LeetCode 26: Remove Duplicates from Sorted Array
Difficulty: Easy
Topics: Array, Two Pointers

Problem:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. The relative order of the elements 
should be kept the same.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array 
in-place with O(1) extra memory.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_ _ _ _ _]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
- 0 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.

Approach:
Use two pointers: slow and fast.
Slow pointer tracks the position of the last unique element.
Fast pointer scans through the array.
When we find a new unique element, we place it after the last unique element.

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) - Constant extra space
"""

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    """
    Remove duplicates from sorted array in-place.
    
    Args:
        nums: Sorted list of integers (modified in-place)
        
    Returns:
        Number of unique elements (k)
    """
    if not nums:
        return 0
    
    # Slow pointer tracks the position of last unique element
    slow = 0
    
    # Fast pointer scans through the array
    for fast in range(1, len(nums)):
        # When we find a new unique element
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    # Return count of unique elements (index + 1)
    return slow + 1

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 1, 2]
    k1 = removeDuplicates(nums1)
    print(f"Test 1: nums = [1,1,2]")
    print(f"Result: k = {k1}, nums = {nums1}")  # Expected: k = 2, nums = [1,2,_]
    assert k1 == 2
    assert nums1[:k1] == [1, 2]
    
    # Test case 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = removeDuplicates(nums2)
    print(f"\nTest 2: nums = [0,0,1,1,1,2,2,3,3,4]")
    print(f"Result: k = {k2}, nums = {nums2}")  # Expected: k = 5, nums = [0,1,2,3,4,_ _ _ _ _]
    assert k2 == 5
    assert nums2[:k2] == [0, 1, 2, 3, 4]
    
    # Test case 3
    nums3 = [1, 1, 1, 1, 1]
    k3 = removeDuplicates(nums3)
    print(f"\nTest 3: nums = [1,1,1,1,1]")
    print(f"Result: k = {k3}, nums = {nums3}")  # Expected: k = 1, nums = [1,_ _ _ _ _]
    assert k3 == 1
    assert nums3[:k3] == [1]
    
    # Test case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = removeDuplicates(nums4)
    print(f"\nTest 4: nums = [1,2,3,4,5]")
    print(f"Result: k = {k4}, nums = {nums4}")  # Expected: k = 5, nums = [1,2,3,4,5]
    assert k4 == 5
    assert nums4[:k4] == [1, 2, 3, 4, 5]
    
    # Test case 5
    nums5 = []
    k5 = removeDuplicates(nums5)
    print(f"\nTest 5: nums = []")
    print(f"Result: k = {k5}, nums = {nums5}")  # Expected: k = 0, nums = []
    assert k5 == 0
    assert nums5[:k5] == []
    
    # Test case 6
    nums6 = [1]
    k6 = removeDuplicates(nums6)
    print(f"\nTest 6: nums = [1]")
    print(f"Result: k = {k6}, nums = {nums6}")  # Expected: k = 1, nums = [1]
    assert k6 == 1
    assert nums6[:k6] == [1]
    
    print("\nAll tests passed!")