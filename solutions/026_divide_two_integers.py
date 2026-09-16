"""
LeetCode 29: Divide Two Integers
Difficulty: Medium
Topics: Math, Bit Manipulation

Problem:
Given two integers dividend and divisor, divide two integers without using multiplication, 
division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within 
the 32-bit signed integer range: [-2^31, 2^31 - 1]. For this problem, if the quotient 
is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly 
less than -2^31, then return -2^31.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Example 3:
Input: dividend = 0, divisor = 1
Output: 0
Explanation: 0/1 = 0

Example 4:
Input: dividend = 1, divisor = 1
Output: 1

Constraints:
- -2^31 <= dividend, divisor <= 2^31 - 1
- divisor != 0

Approach:
Use bit manipulation to perform division efficiently:
1. Handle signs separately
2. Work with absolute values
3. Use doubling strategy (bit shifting) to find largest multiple
4. Subtract and repeat until dividend < divisor
5. Apply sign and handle overflow

Time Complexity: O(log^2(dividend)) - Outer loop O(log n), inner loop O(log n)
Space Complexity: O(1) - Constant extra space
"""

def divide(dividend: int, divisor: int) -> int:
    """
    Divide two integers without using multiplication, division, and mod operator.
    
    Args:
        dividend: Number to be divided
        divisor: Number to divide by
        
    Returns:
        Quotient after division (truncated toward zero)
    """
    # Handle edge cases
    if dividend == 0:
        return 0
    
    if divisor == 1:
        return dividend
    
    if divisor == -1:
        # Handle overflow case
        if dividend > -2**31:
            return -dividend
        else:
            return 2**31 - 1
    
    # Determine sign of the result
    negative = (dividend < 0) != (divisor < 0)
    
    # Work with absolute values
    dividend_abs = abs(dividend)
    divisor_abs = abs(divisor)
    
    quotient = 0
    
    # Use doubling strategy to find quotient efficiently
    while dividend_abs >= divisor_abs:
        # Find the largest multiple of divisor that fits in dividend
        temp = divisor_abs
        multiple = 1
        while dividend_abs >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        
        # Subtract and add to quotient
        dividend_abs -= temp
        quotient += multiple
    
    # Apply sign
    if negative:
        quotient = -quotient
    
    # Handle 32-bit integer overflow
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648
    
    if quotient > INT_MAX:
        return INT_MAX
    elif quotient < INT_MIN:
        return INT_MIN
    else:
        return quotient

# Test cases
if __name__ == "__main__":
    # Test case 1
    dividend1 = 10
    divisor1 = 3
    result1 = divide(dividend1, divisor1)
    print(f"Test 1: dividend = {dividend1}, divisor = {divisor1}")
    print(f"Result: {result1}")  # Expected: 3
    assert result1 == 3
    
    # Test case 2
    dividend2 = 7
    divisor2 = -3
    result2 = divide(dividend2, divisor2)
    print(f"\nTest 2: dividend = {dividend2}, divisor = {divisor2}")
    print(f"Result: {result2}")  # Expected: -2
    assert result2 == -2
    
    # Test case 3
    dividend3 = 0
    divisor3 = 1
    result3 = divide(dividend3, divisor3)
    print(f"\nTest 3: dividend = {dividend3}, divisor = {divisor3}")
    print(f"Result: {result3}")  # Expected: 0
    assert result3 == 0
    
    # Test case 4
    dividend4 = 1
    divisor4 = 1
    result4 = divide(dividend4, divisor4)
    print(f"\nTest 4: dividend = {dividend4}, divisor = {divisor4}")
    print(f"Result: {result4}")  # Expected: 1
    assert result4 == 1
    
    # Additional test cases
    dividend5 = -10
    divisor5 = 3
    result5 = divide(dividend5, divisor5)
    print(f"\nTest 5: dividend = {dividend5}, divisor = {divisor5}")
    print(f"Result: {result5}")  # Expected: -3
    assert result5 == -3
    
    dividend6 = 10
    divisor6 = -3
    result6 = divide(dividend6, divisor6)
    print(f"\nTest 6: dividend = {dividend6}, divisor = {divisor6}")
    print(f"Result: {result6}")  # Expected: -3
    assert result6 == -3
    
    dividend7 = -7
    divisor7 = -3
    result7 = divide(dividend7, divisor7)
    print(f"\nTest 7: dividend = {dividend7}, divisor = {divisor7}")
    print(f"Result: {result7}")  # Expected: 2
    assert result7 == 2
    
    # Test overflow cases
    dividend8 = -2**31
    divisor8 = -1
    result8 = divide(dividend8, divisor8)
    print(f"\nTest 8: dividend = {dividend8}, divisor = {divisor8} (overflow case)")
    print(f"Result: {result8}")  # Expected: 2^31 - 1
    assert result8 == 2**31 - 1
    
    dividend9 = 2**31 - 1
    divisor9 = 1
    result9 = divide(dividend9, divisor9)
    print(f"\nTest 9: dividend = {dividend9}, divisor = {divisor9}")
    print(f"Result: {result9}")  # Expected: 2^31 - 1
    assert result9 == 2**31 - 1
    
    print("\nAll tests passed!")