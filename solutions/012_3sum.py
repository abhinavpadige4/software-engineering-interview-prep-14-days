"""
LeetCode 12: 3Sum
Difficulty: Medium
Topics: Array, Two Pointers, Sorting

Problem:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,-1,2] and [-1,0,1].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
- 0 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

Approach:
1. Sort the array
2. Fix one element and use two pointers to find pairs that sum to the negative of the fixed element
3. Skip duplicates to avoid duplicate triplets in the result

Time Complexity: O(n^2) - Sorting (O(n log n)) + nested loops (O(n^2))
Space Complexity: O(1) or O(n) depending on sorting algorithm (we use O(1) extra space excluding output)
"""

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets in the array that sum up to zero.
    
    Args:
        nums: List of integers
        
    Returns:
        List of unique triplets that sum to zero
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointers approach for the remaining array
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                # Found a triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # Skip duplicates for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers
                left += 1
                right -= 1
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = threeSum(nums1)
    print(f"Test 1: nums = {nums1}")
    print(f"Result: {result1}")  # Expected: [[-1,-1,2],[-1,0,1]]
    # Sort the result for comparison
    result1_sorted = sorted([sorted(triplet) for triplet in result1])
    expected1 = sorted([[-1, -1, 2], [-1, 0, 1]])
    assert result1_sorted == expected1
    
    # Test case 2
    nums2 = [0, 1, 1]
    result2 = threeSum(nums2)
    print(f"\nTest 2: nums = {nums2}")
    print(f"Result: {result2}")  # Expected: []
    assert result2 == []
    
    # Test case 3
    nums3 = [0, 0, 0]
    result3 = threeSum(nums3)
    print(f"\nTest 3: nums = {nums3}")
    print(f"Result: {result3}")  # Expected: [[0,0,0]]
    assert result3 == [[0, 0, 0]]
    
    # Additional test cases
    nums4 = [-2, 0, 1, 1, 2]
    result4 = threeSum(nums4)
    print(f"\nTest 4: nums = {nums4}")
    print(f"Result: {result4}")  # Expected: [[-2,0,2],[-2,1,1]]
    result4_sorted = sorted([sorted(triplet) for triplet in result4])
    expected4 = sorted([[-2, 0, 2], [-2, 1, 1]])
    assert result4_sorted == expected4
    
    nums5 = [3, 0, -2, -1, 1, 2]
    result5 = threeSum(nums5)
    print(f"\nTest 5: nums = {nums5}")
    print(f"Result: {result5}")  # Expected: [[-2,-1,3],[-2,0,2],[-1,0,1]]
    result5_sorted = sorted([sorted(triplet) for triplet in result5])
    expected5 = sorted([[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]])
    assert result5_sorted == expected5
    
    print("\nAll tests passed!")