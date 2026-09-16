"""
LeetCode 20: Valid Parentheses
Difficulty: Easy
Topics: String, Stack

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.

Approach:
Use a stack to keep track of opening brackets.
When we encounter a closing bracket, check if it matches the top of the stack.
If it matches, pop from stack; otherwise, return false.
At the end, the stack should be empty for valid parentheses.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for the stack in worst case
"""

def isValid(s: str) -> bool:
    """
    Determine if a string of parentheses is valid.
    
    Args:
        s: String containing only parentheses characters
        
    Returns:
        True if the string is valid, False otherwise
    """
    # Stack to keep track of opening brackets
    stack = []
    
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        # If it's an opening bracket, push to stack
        if char in bracket_map.values():
            stack.append(char)
        # If it's a closing bracket
        elif char in bracket_map:
            # If stack is empty or top doesn't match, return False
            if not stack or stack[-1] != bracket_map[char]:
                return False
            # Pop the matching opening bracket
            stack.pop()
        # Ignore any other characters (though problem says only parentheses)
    
    # If stack is empty, all brackets were properly closed
    return len(stack) == 0

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "()"
    result1 = isValid(s1)
    print(f"Test 1: s = '{s1}'")
    print(f"Result: {result1}")  # Expected: True
    assert result1 == True
    
    # Test case 2
    s2 = "()[]{}"
    result2 = isValid(s2)
    print(f"\nTest 2: s = '{s2}'")
    print(f"Result: {result2}")  # Expected: True
    assert result2 == True
    
    # Test case 3
    s3 = "(]"
    result3 = isValid(s3)
    print(f"\nTest 3: s = '{s3}'")
    print(f"Result: {result3}")  # Expected: False
    assert result3 == False
    
    # Test case 4
    s4 = "([)]"
    result4 = isValid(s4)
    print(f"\nTest 4: s = '{s4}'")
    print(f"Result: {result4}")  # Expected: False
    assert result4 == False
    
    # Test case 5
    s5 = "{[]}"
    result5 = isValid(s5)
    print(f"\nTest 5: s = '{s5}'")
    print(f"Result: {result5}")  # Expected: True
    assert result5 == True
    
    # Additional test cases
    s6 = ""
    result6 = isValid(s6)
    print(f"\nTest 6: s = '{s6}' (empty string)")
    print(f"Result: {result6}")  # Expected: True
    assert result6 == True
    
    s7 = "((()))"
    result7 = isValid(s7)
    print(f"\nTest 7: s = '{s7}'")
    print(f"Result: {result7}")  # Expected: True
    assert result7 == True
    
    s8 = "({[()]})"
    result8 = isValid(s8)
    print(f"\nTest 8: s = '{s8}'")
    print(f"Result: {result8}")  # Expected: True
    assert result8 == True
    
    s9 = "({[)]}"
    result9 = isValid(s9)
    print(f"\nTest 9: s = '{s9}'")
    print(f"Result: {result9}")  # Expected: False
    assert result9 == False
    
    s10 = "[[{{(())}}]]"
    result10 = isValid(s10)
    print(f"\nTest 10: s = '{s10}'")
    print(f"Result: {result10}")  # Expected: True
    assert result10 == True
    
    print("\nAll tests passed!")