"""
LeetCode 13: 3Sum Closest
Difficulty: Medium
Topics: Array, Two Pointers, Sorting

Problem:
Given an integer array nums of length n and an integer target, find three integers in nums 
such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Constraints:
- 3 <= nums.length <= 1000
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4

Approach:
Similar to 3Sum problem:
1. Sort the array
2. Fix one element and use two pointers to find pairs
3. Track the closest sum instead of exact matches
4. Move pointers based on whether current sum is less than or greater than target

Time Complexity: O(n^2) - Sorting (O(n log n)) + nested loops (O(n^2))
Space Complexity: O(1) or O(n) depending on sorting algorithm
"""

from typing import List
import math

def threeSumClosest(nums: List[int], target: int) -> int:
    """
    Find three integers in nums such that the sum is closest to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        Sum of three integers closest to target
    """
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')
    
    for i in range(n - 2):
        # Two pointers approach
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            # Update closest sum if current is closer to target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            # Move pointers based on comparison with target
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # Exact match found
                return current_sum
    
    return closest_sum

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [-1, 2, 1, -4]
    target1 = 1
    result1 = threeSumClosest(nums1, target1)
    print(f"Test 1: nums = {nums1}, target = {target1}")
    print(f"Result: {result1}")  # Expected: 2
    assert result1 == 2
    
    # Test case 2
    nums2 = [0, 0, 0]
    target2 = 1
    result2 = threeSumClosest(nums2, target2)
    print(f"\nTest 2: nums = {nums2}, target = {target2}")
    print(f"Result: {result2}")  # Expected: 0
    assert result2 == 0
    
    # Test case 3
    nums3 = [1, 1, 1, 0]
    target3 = -100
    result3 = threeSumClosest(nums3, target3)
    print(f"\nTest 3: nums = {nums3}, target = {target3}")
    print(f"Result: {result3}")  # Expected: 2
    assert result3 == 2
    
    # Test case 4
    nums4 = [1, 2, 4, 8, 16, 32, 64, 128]
    target4 = 82
    result4 = threeSumClosest(nums4, target4)
    print(f"\nTest 4: nums = {nums4}, target = {target4}")
    print(f"Result: {result4}")  # Expected: 82
    assert result4 == 82
    
    # Additional test cases
    nums5 = [-3, -2, -1, 0, 0, 1, 2, 3]
    target5 = 0
    result5 = threeSumClosest(nums5, target5)
    print(f"\nTest 5: nums = {nums5}, target = {target5}")
    print(f"Result: {result5}")  # Expected: 0
    assert result5 == 0
    
    nums6 = [1, 2, 5, 10, 11]
    target6 = 12
    result6 = threeSumClosest(nums6, target6)
    print(f"\nTest 6: nums = {nums6}, target = {target6}")
    print(f"Result: {result6}")  # Expected: 13
    assert result6 == 13
    
    print("\nAll tests passed!")