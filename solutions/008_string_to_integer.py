"""
LeetCode 8: String to Integer (atoi)
Difficulty: Medium
Topics: String

Problem:
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:
1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. 
   Read this character in if it is either. This determines if the final result is negative or positive respectively. 
   Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached. 
   The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
   If no digits were read, then the integer is 0.
5. Change the sign as necessary (from step 2).
6. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer 
   so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, 
   and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
7. Return the integer as the final result.

Note:
- Only the space character ' ' is considered a whitespace character.
- Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Example 1:
Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Step 4: 42
         ^
Step 5: 42
         ^
Step 6: 42
         ^
Step 7: Return 42

Example 2:
Input: s = "   -42"
Output: -42
Explanation: 
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read in)
             ^
Step 3: "   -42" ("42" is read in)
               ^
Step 4: -42
         ^
Step 5: -42
         ^
Step 6: -42
         ^
Step 7: Return -42

Example 3:
Input: s = "4193 with words"
Output: 4193
Explanation: 
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in)
              ^
Step 4: 4193
         ^
Step 5: 4193
         ^
Step 6: 4193
         ^
Step 7: Return 4193

Example 4:
Input: s = "words and 987"
Output: 0
Explanation: 
Step 1: "words and 987" (no characters read because there is no leading whitespace)
         ^
Step 2: "words and 987" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "words and 987" (reading stops at the first non-digit character 'w')
         ^
Step 4: 0
         ^
Step 5: 0
         ^
Step 6: 0
         ^
Step 7: Return 0

Example 5:
Input: s = "-91283472332"
Output: -2147483648
Explanation: 
Step 1: "-91283472332" (no characters read because there is no leading whitespace)
         ^
Step 2: "-91283472332" ('-' is read in)
             ^
Step 3: "-91283472332" ("91283472332" is read in)
                           ^
Step 4: -91283472332
         ^
Step 5: -91283472332
         ^
Step 6: -2147483648 (clamped due to overflow)
         ^
Step 7: Return -2147483648

Constraints:
- 0 <= s.length <= 200
- s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

Approach:
Follow the algorithm steps precisely:
1. Skip leading whitespace
2. Check for sign
3. Read digits until non-digit
4. Convert to integer with overflow checking
5. Apply sign and clamp to 32-bit range

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1) - Constant extra space
"""

def myAtoi(s: str) -> int:
    """
    Convert a string to a 32-bit signed integer.
    
    Args:
        s: Input string
        
    Returns:
        32-bit signed integer representation of the string
    """
    # Define 32-bit integer limits
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648
    
    # Step 1: Skip leading whitespace
    i = 0
    n = len(s)
    while i < n and s[i] == ' ':
        i += 1
    
    # If we reached the end, return 0
    if i == n:
        return 0
    
    # Step 2: Check for sign
    sign = 1
    if s[i] == '-':
        sign = -1
        i += 1
    elif s[i] == '+':
        i += 1
    
    # Step 3: Read digits
    result = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        
        # Step 4 & 5: Check for overflow before adding digit
        # For positive: result * 10 + digit <= INT_MAX
        # For negative: -(result * 10 + digit) >= INT_MIN
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        
        result = result * 10 + digit
        i += 1
    
    # Step 6: Apply sign
    return sign * result

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "42"
    result1 = myAtoi(s1)
    print(f"Test 1: s = '{s1}'")
    print(f"Result: {result1}")  # Expected: 42
    assert result1 == 42
    
    # Test case 2
    s2 = "   -42"
    result2 = myAtoi(s2)
    print(f"\nTest 2: s = '{s2}'")
    print(f"Result: {result2}")  # Expected: -42
    assert result2 == -42
    
    # Test case 3
    s3 = "4193 with words"
    result3 = myAtoi(s3)
    print(f"\nTest 3: s = '{s3}'")
    print(f"Result: {result3}")  # Expected: 4193
    assert result3 == 4193
    
    # Test case 4
    s4 = "words and 987"
    result4 = myAtoi(s4)
    print(f"\nTest 4: s = '{s4}'")
    print(f"Result: {result4}")  # Expected: 0
    assert result4 == 0
    
    # Test case 5
    s5 = "-91283472332"
    result5 = myAtoi(s5)
    print(f"\nTest 5: s = '{s5}'")
    print(f"Result: {result5}")  # Expected: -2147483648
    assert result5 == -2147483648
    
    # Additional test cases
    s6 = "   +42"
    result6 = myAtoi(s6)
    print(f"\nTest 6: s = '{s6}'")
    print(f"Result: {result6}")  # Expected: 42
    assert result6 == 42
    
    s7 = "00000-42a1234"
    result7 = myAtoi(s7)
    print(f"\nTest 7: s = '{s7}'")
    print(f"Result: {result7}")  # Expected: 0
    assert result7 == 0
    
    s8 = "-5-"
    result8 = myAtoi(s8)
    print(f"\nTest 8: s = '{s8}'")
    print(f"Result: {result8}")  # Expected: -5
    assert result8 == -5
    
    s9 = "2147483648"
    result9 = myAtoi(s9)
    print(f"\nTest 9: s = '{s9}'")
    print(f"Result: {result9}")  # Expected: 2147483647 (clamped)
    assert result9 == 2147483647
    
    print("\nAll tests passed!")