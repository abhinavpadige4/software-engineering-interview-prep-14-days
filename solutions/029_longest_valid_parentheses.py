"""
LeetCode 32: Longest Valid Parentheses
Difficulty: Hard
Topics: String, Stack, Dynamic Programming

Problem:
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

Constraints:
- 0 <= s.length <= 3 * 10^4
- s consists of '(' and/or ')' only.

Approach:
Use stack to track indices of unmatched parentheses:
1. Push -1 onto stack as base
2. When we see '(', push its index
3. When we see ')', pop from stack
4. If stack becomes empty, push current index as new base
5. Otherwise, calculate length from current index to top of stack
6. Keep track of maximum length found

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for the stack
"""

def longestValidParentheses(s: str) -> int:
    """
    Find the length of the longest valid parentheses substring.
    
    Args:
        s: String containing only '(' and ')'
        
    Returns:
        Length of the longest valid parentheses substring
    """
    max_length = 0
    stack = [-1]  # Initialize with -1 as base for first valid substring
    
    for i, char in enumerate(s):
        if char == '(':
            # Push index of '(' onto stack
            stack.append(i)
        else:  # char == ')'
            # Pop the top element
            stack.pop()
            
            if not stack:
                # If stack is empty, push current index as base
                stack.append(i)
            else:
                # Calculate length of current valid substring
                current_length = i - stack[-1]
                max_length = max(max_length, current_length)
    
    return max_length

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "(()"
    result1 = longestValidParentheses(s1)
    print(f"Test 1: s = '{s1}'")
    print(f"Result: {result1}")  # Expected: 2
    assert result1 == 2
    
    # Test case 2
    s2 = ")()())"
    result2 = longestValidParentheses(s2)
    print(f"\nTest 2: s = '{s2}'")
    print(f"Result: {result2}")  # Expected: 4
    assert result2 == 4
    
    # Test case 3
    s3 = ""
    result3 = longestValidParentheses(s3)
    print(f"\nTest 3: s = '{s3}'")
    print(f"Result: {result3}")  # Expected: 0
    assert result3 == 0
    
    # Additional test cases
    s4 = "()(()"
    result4 = longestValidParentheses(s4)
    print(f"\nTest 4: s = '{s4}'")
    print(f"Result: {result4}")  # Expected: 2
    assert result4 == 2
    
    s5 = "()(())"
    result5 = longestValidParentheses(s5)
    print(f"\nTest 5: s = '{s5}'")
    print(f"Result: {result5}")  # Expected: 6
    assert result5 == 6
    
    s6 = "((()))"
    result6 = longestValidParentheses(s6)
    print(f"\nTest 6: s = '{s6}'")
    print(f"Result: {result6}")  # Expected: 6
    assert result6 == 6
    
    s7 = ")()())()()("
    result7 = longestValidParentheses(s7)
    print(f"\nTest 7: s = '{s7}'")
    print(f"Result: {result7}")  # Expected: 8
    assert result7 == 8
    
    s8 = "((((())"
    result8 = longestValidParentheses(s8)
    print(f"\nTest 8: s = '{s8}'")
    print(f"Result: {result8}")  # Expected: 4
    assert result8 == 4
    
    print("\nAll tests passed!")