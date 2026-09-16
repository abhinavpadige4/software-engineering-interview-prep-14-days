"""
LeetCode 11: Container With Most Water
Difficulty: Medium
Topics: Array, Two Pointers, Greedy

Problem:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Approach:
Use two pointers starting from both ends. Calculate the area and move the pointer 
pointing to the shorter line inward. This works because moving the pointer at the 
longer line inward would never increase the area (width decreases and height is 
limited by the shorter line).

Time Complexity: O(n) - Single pass with two pointers
Space Complexity: O(1) - Constant extra space
"""

from typing import List

def maxArea(height: List[int]) -> int:
    """
    Find the maximum area of water that can be contained.
    
    Args:
        height: List of heights of vertical lines
        
    Returns:
        Maximum area of water that can be contained
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        max_area = max(max_area, current_area)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Test cases
if __name__ == "__main__":
    # Test case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result1 = maxArea(height1)
    print(f"Test 1: height = {height1}")
    print(f"Result: {result1}")  # Expected: 49
    assert result1 == 49
    
    # Test case 2
    height2 = [1, 1]
    result2 = maxArea(height2)
    print(f"\nTest 2: height = {height2}")
    print(f"Result: {result2}")  # Expected: 1
    assert result2 == 1
    
    # Test case 3
    height3 = [4, 3, 2, 1, 4]
    result3 = maxArea(height3)
    print(f"\nTest 3: height = {height3}")
    print(f"Result: {result3}")  # Expected: 16
    assert result3 == 16
    
    # Test case 4
    height4 = [1, 2, 1]
    result4 = maxArea(height4)
    print(f"\nTest 4: height = {height4}")
    print(f"Result: {result4}")  # Expected: 2
    assert result4 == 2
    
    # Additional test cases
    height5 = [1, 2, 4, 3]
    result5 = maxArea(height5)
    print(f"\nTest 5: height = {height5}")
    print(f"Result: {result5}")  # Expected: 4
    assert result5 == 4
    
    height6 = [2, 3, 4, 5, 18, 17, 6]
    result6 = maxArea(height6)
    print(f"\nTest 6: height = {height6}")
    print(f"Result: {result6}")  # Expected: 17
    assert result6 == 17
    
    print("\nAll tests passed!")