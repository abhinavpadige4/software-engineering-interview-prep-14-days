"""
LeetCode 9: Palindrome Number
Difficulty: Easy
Topics: Math

Problem:
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false

Constraints:
-2^31 <= x <= 2^31 - 1

Approach:
Negative numbers are not palindromes due to the minus sign.
For positive numbers, we can reverse half of the number and compare it with the other half.
To avoid overflow, we reverse only half of the digits.

Time Complexity: O(log10(x)) - Number of digits in x
Space Complexity: O(1) - Constant extra space
"""

def isPalindrome(x: int) -> bool:
    """
    Check if an integer is a palindrome.
    
    Args:
        x: Integer to check
        
    Returns:
        True if x is palindrome, False otherwise
    """
    # Negative numbers are not palindromes
    # Numbers ending with 0 (except 0 itself) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    # Special case for 0
    if x == 0:
        return True
    
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    # When the length is an odd number, we can get rid of the middle digit by reversed_half // 10
    # For example, when the input is 12321, at the end of the while loop we get x = 12, reversed_half = 123,
    # since the middle digit (3) doesn't matter in palindrome (it will always equal to itself), we can simply remove it.
    return x == reversed_half or x == reversed_half // 10

# Test cases
if __name__ == "__main__":
    # Test case 1
    x1 = 121
    result1 = isPalindrome(x1)
    print(f"Test 1: x = {x1}")
    print(f"Result: {result1}")  # Expected: True
    assert result1 == True
    
    # Test case 2
    x2 = -121
    result2 = isPalindrome(x2)
    print(f"\nTest 2: x = {x2}")
    print(f"Result: {result2}")  # Expected: False
    assert result2 == False
    
    # Test case 3
    x3 = 10
    result3 = isPalindrome(x3)
    print(f"\nTest 3: x = {x3}")
    print(f"Result: {result3}")  # Expected: False
    assert result3 == False
    
    # Test case 4
    x4 = -101
    result4 = isPalindrome(x4)
    print(f"\nTest 4: x = {x4}")
    print(f"Result: {result4}")  # Expected: False
    assert result4 == False
    
    # Additional test cases
    x5 = 0
    result5 = isPalindrome(x5)
    print(f"\nTest 5: x = {x5}")
    print(f"Result: {result5}")  # Expected: True
    assert result5 == True
    
    x6 = 12321
    result6 = isPalindrome(x6)
    print(f"\nTest 6: x = {x6}")
    print(f"Result: {result6}")  # Expected: True
    assert result6 == True
    
    x7 = 123
    result7 = isPalindrome(x7)
    print(f"\nTest 7: x = {x7}")
    print(f"Result: {result7}")  # Expected: False
    assert result7 == False
    
    x8 = 1
    result8 = isPalindrome(x8)
    print(f"\nTest 8: x = {x8}")
    print(f"Result: {result8}")  # Expected: True
    assert result8 == True
    
    x9 = 11
    result9 = isPalindrome(x9)
    print(f"\nTest 9: x = {x9}")
    print(f"Result: {result9}")  # Expected: True
    assert result9 == True
    
    x10 = 1001
    result10 = isPalindrome(x10)
    print(f"\nTest 10: x = {x10}")
    print(f"Result: {result10}")  # Expected: True
    assert result10 == True
    
    print("\nAll tests passed!")