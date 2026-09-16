"""
LeetCode 31: Next Permutation
Difficulty: Medium
Topics: Array, Two Pointers

Problem:
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: 
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container. 
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100

Approach:
1. Find the first decreasing element from right (nums[i] < nums[i+1])
2. Find the first element from right that is greater than nums[i]
3. Swap these two elements
4. Reverse the subarray to the right of the original position of nums[i]

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) - Constant extra space
"""

from typing import List

def nextPermutation(nums: List[int]) -> None:
    """
    Rearrange numbers into the lexicographically next greater permutation.
    
    Args:
        nums: List of integers (modified in-place)
        
    Returns:
        None (modifies nums in-place)
    """
    # Find the first decreasing element from right
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    # If we found such an element
    if i >= 0:
        # Find the first element from right that is greater than nums[i]
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        
        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
    
    # Reverse the subarray to the right of position i
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3]
    nextPermutation(nums1)
    print(f"Test 1: nums = [1,2,3]")
    print(f"Result: {nums1}")  # Expected: [1,3,2]
    assert nums1 == [1, 3, 2]
    
    # Test case 2
    nums2 = [3, 2, 1]
    nextPermutation(nums2)
    print(f"\nTest 2: nums = [3,2,1]")
    print(f"Result: {nums2}")  # Expected: [1,2,3]
    assert nums2 == [1, 2, 3]
    
    # Test case 3
    nums3 = [1, 1, 5]
    nextPermutation(nums3)
    print(f"\nTest 3: nums = [1,1,5]")
    print(f"Result: {nums3}")  # Expected: [1,5,1]
    assert nums3 == [1, 5, 1]
    
    # Additional test cases
    nums4 = [1, 3, 2]
    nextPermutation(nums4)
    print(f"\nTest 4: nums = [1,3,2]")
    print(f"Result: {nums4}")  # Expected: [2,1,3]
    assert nums4 == [2, 1, 3]
    
    nums5 = [2, 3, 1]
    nextPermutation(nums5)
    print(f"\nTest 5: nums = [2,3,1]")
    print(f"Result: {nums5}")  # Expected: [3,1,2]
    assert nums5 == [3, 1, 2]
    
    nums6 = [1, 2, 3, 4]
    nextPermutation(nums6)
    print(f"\nTest 6: nums = [1,2,3,4]")
    print(f"Result: {nums6}")  # Expected: [1,2,4,3]
    assert nums6 == [1, 2, 4, 3]
    
    nums7 = [4, 3, 2, 1]
    nextPermutation(nums7)
    print(f"\nTest 7: nums = [4,3,2,1]")
    print(f"Result: {nums7}")  # Expected: [1,2,3,4]
    assert nums7 == [1, 2, 3, 4]
    
    nums8 = [1, 1, 1]
    nextPermutation(nums8)
    print(f"\nTest 8: nums = [1,1,1]")
    print(f"Result: {nums8}")  # Expected: [1,1,1] (already highest)
    assert nums8 == [1, 1, 1]
    
    nums9 = [1]
    nextPermutation(nums9)
    print(f"\nTest 9: nums = [1]")
    print(f"Result: {nums9}")  # Expected: [1]
    assert nums9 == [1]
    
    print("\nAll tests passed!")