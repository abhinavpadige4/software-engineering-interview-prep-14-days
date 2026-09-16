"""
LeetCode 1: Two Sum
Difficulty: Easy
Topics: Array, Hash Table

Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Approach:
Use a hash map to store the complement of each number (target - num) as we iterate through the array.
For each number, check if it exists in the hash map. If yes, we found our pair.

Time Complexity: O(n) - We traverse the list containing n elements only once.
Space Complexity: O(n) - The space required depends on the number of items stored in the hash map.
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers in the array that add up to the target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing indices of the two numbers that add up to target
    """
    # Hash map to store number -> index mapping
    num_map = {}
    
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach target
        complement = target - num
        
        # If complement exists in map, we found the solution
        if complement in num_map:
            return [num_map[complement], i]
        
        # Store current number's index
        num_map[num] = i
    
    # According to problem constraints, this line should never be reached
    return []

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Result: {result1}")  # Expected: [0, 1]
    assert result1 == [0, 1] or result1 == [1, 0]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"\nTest 2: nums={nums2}, target={target2}")
    print(f"Result: {result2}")  # Expected: [1, 2]
    assert result2 == [1, 2] or result2 == [2, 1]
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum(nums3, target3)
    print(f"\nTest 3: nums={nums3}, target={target3}")
    print(f"Result: {result3}")  # Expected: [0, 1]
    assert result3 == [0, 1] or result3 == [1, 0]
    
    print("\nAll tests passed!")