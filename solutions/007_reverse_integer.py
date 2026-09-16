"""
LeetCode 7: Reverse Integer
Difficulty: Medium
Topics: Math

Problem:
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

Constraints:
-2^31 <= x <= 2^31 - 1

Approach:
Extract digits from the end using modulo and division operations.
Build the reversed number while checking for overflow at each step.
Handle negative numbers by working with absolute value and restoring sign.

Time Complexity: O(log(x)) - Number of digits in x
Space Complexity: O(1) - Constant extra space
"""

def reverse(x: int) -> int:
    """
    Reverse the digits of a signed 32-bit integer.
    
    Args:
        x: Integer to reverse
        
    Returns:
        Reversed integer, or 0 if overflow occurs
    """
    # Define 32-bit integer limits
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648
    
    # Store the sign and work with absolute value
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    
    reversed_num = 0
    
    while x_abs != 0:
        # Extract the last digit
        digit = x_abs % 10
        x_abs //= 10
        
        # Check for overflow before adding the digit
        # For positive: reversed_num * 10 + digit <= INT_MAX
        # For negative: -(reversed_num * 10 + digit) >= INT_MIN
        if reversed_num > (INT_MAX - digit) // 10:
            return 0
        
        # Add the digit to reversed number
        reversed_num = reversed_num * 10 + digit
    
    # Apply the original sign
    return sign * reversed_num

# Test cases
if __name__ == "__main__":
    # Test case 1
    x1 = 123
    result1 = reverse(x1)
    print(f"Test 1: x = {x1}")
    print(f"Result: {result1}")  # Expected: 321
    assert result1 == 321
    
    # Test case 2
    x2 = -123
    result2 = reverse(x2)
    print(f"\nTest 2: x = {x2}")
    print(f"Result: {result2}")  # Expected: -321
    assert result2 == -321
    
    # Test case 3
    x3 = 120
    result3 = reverse(x3)
    print(f"\nTest 3: x = {x3}")
    print(f"Result: {result3}")  # Expected: 21
    assert result3 == 21
    
    # Test case 4
    x4 = 0
    result4 = reverse(x4)
    print(f"\nTest 4: x = {x4}")
    print(f"Result: {result4}")  # Expected: 0
    assert result4 == 0
    
    # Test case 5: Overflow case
    x5 = 1534236469
    result5 = reverse(x5)
    print(f"\nTest 5: x = {x5} (overflow case)")
    print(f"Result: {result5}")  # Expected: 0
    assert result5 == 0
    
    # Test case 6: Negative overflow case
    x6 = -2147483412
    result6 = reverse(x6)
    print(f"\nTest 6: x = {x6} (negative overflow case)")
    print(f"Result: {result6}")  # Expected: 0
    assert result6 == 0
    
    # Test case 7: Edge case -2^31
    x7 = -2147483648
    result7 = reverse(x7)
    print(f"\nTest 7: x = {x7} (INT_MIN)")
    print(f"Result: {result7}")  # Expected: 0
    assert result7 == 0
    
    print("\nAll tests passed!")