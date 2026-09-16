"""
LeetCode 18: 4Sum
Difficulty: Medium
Topics: Array, Two Pointers, Sorting

Problem:
Given an array nums of n integers, return an array of all the unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:
- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
- 1 <= nums.length <= 200
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9

Approach:
Extension of 3Sum approach:
1. Sort the array
2. Fix two elements using nested loops
3. Use two pointers to find pairs that sum to the remaining target
4. Skip duplicates to avoid duplicate quadruplets

Time Complexity: O(n^3) - Sorting (O(n log n)) + triple nested loops (O(n^3))
Space Complexity: O(1) or O(n) depending on sorting algorithm
"""

from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all unique quadruplets in the array that sum up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of unique quadruplets that sum to target
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 3):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Optimization: if the smallest possible sum is greater than target, break
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        
        # Optimization: if the largest possible sum is less than target, continue
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue
        
        for j in range(i + 1, n - 2):
            # Skip duplicate values for the second element
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            # Two pointers approach for the remaining array
            left, right = j + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # Found a quadruplet
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    # Skip duplicates for the third element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicates for the fourth element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers
                    left += 1
                    right -= 1
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    result1 = fourSum(nums1, target1)
    print(f"Test 1: nums = {nums1}, target = {target1}")
    print(f"Result: {sorted([sorted(quad) for quad in result1])}")  # Expected: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    expected1 = sorted([sorted(quad) for quad in [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]])
    assert sorted([sorted(quad) for quad in result1]) == expected1
    
    # Test case 2
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    result2 = fourSum(nums2, target2)
    print(f"\nTest 2: nums = {nums2}, target = {target2}")
    print(f"Result: {result2}")  # Expected: [[2,2,2,2]]
    assert result2 == [[2, 2, 2, 2]]
    
    # Test case 3
    nums3 = [0, 0, 0, 0]
    target3 = 0
    result3 = fourSum(nums3, target3)
    print(f"\nTest 3: nums = {nums3}, target = {target3}")
    print(f"Result: {result3}")  # Expected: [[0,0,0,0]]
    assert result3 == [[0, 0, 0, 0]]
    
    # Additional test cases
    nums4 = [-3, -2, -1, 0, 0, 1, 2, 3]
    target4 = 0
    result4 = fourSum(nums4, target4)
    print(f"\nTest 4: nums = {nums4}, target = {target4}")
    print(f"Number of quadruplets: {len(result4)}")
    # Should have multiple valid quadruplets
    assert len(result4) > 0
    
    nums5 = [1, 0, -1, 0, -2, 2]
    target5 = -1
    result5 = fourSum(nums5, target5)
    print(f"\nTest 5: nums = {nums5}, target = {target5}")
    print(f"Result: {sorted([sorted(quad) for quad in result5])}")
    # Should find valid quadruplets
    assert isinstance(result5, list)
    
    print("\nAll tests passed!")