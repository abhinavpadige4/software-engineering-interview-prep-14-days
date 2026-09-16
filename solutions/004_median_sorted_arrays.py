"""
LeetCode 4: Median of Two Sorted Arrays
Difficulty: Hard
Topics: Array, Binary Search, Divide and Conquer

Problem:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6

Approach:
Use binary search on the smaller array to find the correct partition.
We want to partition both arrays such that:
- Left part has equal or one more element than right part
- All elements in left part <= all elements in right part

Time Complexity: O(log(min(m, n))) - Binary search on the smaller array
Space Complexity: O(1) - Constant extra space
"""

from typing import List

def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Find the median of two sorted arrays.
    
    Args:
        nums1: First sorted array
        nums2: Second sorted array
        
    Returns:
        Median of the two sorted arrays as a float
    """
    # Ensure nums1 is the smaller array for efficiency
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    total = m + n
    half = total // 2
    
    # Binary search on the smaller array
    left, right = 0, m
    
    while left <= right:
        # Partition nums1 at i
        i = (left + right) // 2
        # Partition nums2 at j
        j = half - i
        
        # Get values around the partitions
        nums1_left = float('-inf') if i == 0 else nums1[i - 1]
        nums1_right = float('inf') if i == m else nums1[i]
        nums2_left = float('-inf') if j == 0 else nums2[j - 1]
        nums2_right = float('inf') if j == n else nums2[j]
        
        # Check if we found the correct partition
        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            # Even total length
            if total % 2 == 0:
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            # Odd total length
            else:
                return min(nums1_right, nums2_right)
        elif nums1_left > nums2_right:
            # We're too far right in nums1, move left
            right = i - 1
        else:
            # We're too far left in nums1, move right
            left = i + 1
    
    # This line should never be reached given the constraints
    return 0.0

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 3]
    nums2 = [2]
    result = find_median_sorted_arrays(nums1, nums2)
    print(f"Test 1: nums1={nums1}, nums2={nums2}")
    print(f"Result: {result}")  # Expected: 2.0
    assert abs(result - 2.0) < 1e-5
    
    # Test case 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = find_median_sorted_arrays(nums1, nums2)
    print(f"\nTest 2: nums1={nums1}, nums2={nums2}")
    print(f"Result: {result}")  # Expected: 2.5
    assert abs(result - 2.5) < 1e-5
    
    # Test case 3: One empty array
    nums1 = []
    nums2 = [1]
    result = find_median_sorted_arrays(nums1, nums2)
    print(f"\nTest 3: nums1={nums1}, nums2={nums2}")
    print(f"Result: {result}")  # Expected: 1.0
    assert abs(result - 1.0) < 1e-5
    
    # Test case 4: Both arrays have elements
    nums1 = [1, 3, 8, 9, 15]
    nums2 = [7, 11, 18, 19, 21, 25]
    result = find_median_sorted_arrays(nums1, nums2)
    print(f"\nTest 4: nums1={nums1}, nums2={nums2}")
    print(f"Result: {result}")  # Expected: 11.0
    assert abs(result - 11.0) < 1e-5
    
    print("\nAll tests passed!")