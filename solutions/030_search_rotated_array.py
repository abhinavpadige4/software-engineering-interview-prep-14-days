"""
LeetCode 33: Search in Rotated Sorted Array
Difficulty: Medium
Topics: Array, Binary Search

Problem:
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, 
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Explanation: The target 0 is at index 4 in nums.

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Explanation: The target 3 is not in nums.

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique.
- nums is an ascending array that is possibly rotated.
- -10^4 <= target <= 10^4

Approach:
Use modified binary search:
1. Find the middle element
2. Determine which half is sorted
3. Check if target lies in the sorted half
4. If yes, search in that half; otherwise, search in the other half
5. Repeat until target is found or search space is exhausted

Time Complexity: O(log n) where n is the length of the array
Space Complexity: O(1) - Constant extra space
"""

from typing import List

def search(nums: List[int], target: int) -> int:
    """
    Search for target in a rotated sorted array.
    
    Args:
        nums: Rotated sorted array with distinct values
        target: Target value to search for
        
    Returns:
        Index of target if found, otherwise -1
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If we found the target
        if nums[mid] == target:
            return mid
        
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                # Target is in left half
                right = mid - 1
            else:
                # Target is in right half
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                # Target is in right half
                left = mid + 1
            else:
                # Target is in left half
                right = mid - 1
    
    # Target not found
    return -1

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    result1 = search(nums1, target1)
    print(f"Test 1: nums = {nums1}, target = {target1}")
    print(f"Result: {result1}")  # Expected: 4
    assert result1 == 4
    
    # Test case 2
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    result2 = search(nums2, target2)
    print(f"\nTest 2: nums = {nums2}, target = {target2}")
    print(f"Result: {result2}")  # Expected: -1
    assert result2 == -1
    
    # Test case 3
    nums3 = [1]
    target3 = 0
    result3 = search(nums3, target3)
    print(f"\nTest 3: nums = {nums3}, target = {target3}")
    print(f"Result: {result3}")  # Expected: -1
    assert result3 == -1
    
    # Additional test cases
    nums4 = [4, 5, 6, 7, 0, 1, 2]
    target4 = 5
    result4 = search(nums4, target4)
    print(f"\nTest 4: nums = {nums4}, target = {target4}")
    print(f"Result: {result4}")  # Expected: 1
    assert result4 == 1
    
    nums5 = [5, 1, 3]
    target5 = 3
    result5 = search(nums5, target5)
    print(f"\nTest 5: nums = {nums5}, target = {target5}")
    print(f"Result: {result5}")  # Expected: 2
    assert result5 == 2
    
    nums6 = [5, 1, 3]
    target6 = 5
    result6 = search(nums6, target6)
    print(f"\nTest 6: nums = {nums6}, target = {target6}")
    print(f"Result: {result6}")  # Expected: 0
    assert result6 == 0
    
    nums7 = [3, 5, 1]
    target7 = 3
    result7 = search(nums7, target7)
    print(f"\nTest 7: nums = {nums7}, target = {target7}")
    print(f"Result: {result7}")  # Expected: 0
    assert result7 == 0
    
    nums8 = [3, 1]
    target8 = 1
    result8 = search(nums8, target8)
    print(f"\nTest 8: nums = {nums8}, target = {target8}")
    print(f"Result: {result8}")  # Expected: 1
    assert result8 == 1
    
    nums9 = [1, 3]
    target9 = 3
    result9 = search(nums9, target9)
    print(f"\nTest 9: nums = {nums9}, target = {target9}")
    print(f"Result: {result9}")  # Expected: 1
    assert result9 == 1
    
    nums10 = [6, 7, 1, 2, 3, 4, 5]
    target10 = 2
    result10 = search(nums10, target10)
    print(f"\nTest 10: nums = {nums10}, target = {target10}")
    print(f"Result: {result10}")  # Expected: 3
    assert result10 == 3
    
    print("\nAll tests passed!")