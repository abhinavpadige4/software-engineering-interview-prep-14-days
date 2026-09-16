"""
LeetCode 10: Regular Expression Matching
Difficulty: Hard
Topics: String, Dynamic Programming, Recursion

Problem:
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. 
Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. 
Therefore it matches "aab".

Example 5:
Input: s = "mississippi", p = "mis*is*p*."
Output: false

Constraints:
- 0 <= s.length <= 20
- 0 <= p.length <= 30
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.
- It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

Approach:
Use dynamic programming with memoization (top-down) or bottom-up DP.
dp[i][j] represents whether s[i:] matches p[j:].

Base cases:
- dp[len(s)][len(p)] = True (empty string matches empty pattern)
- dp[i][len(p)] = False for i < len(s) (non-empty string doesn't match empty pattern)
- dp[len(s)][j] needs to be calculated based on pattern

Transition:
If p[j+1] is '*':
  dp[i][j] = dp[i][j+2] (zero occurrences) OR 
             (first_match and dp[i+1][j]) (one or more occurrences)
Else:
  dp[i][j] = first_match and dp[i+1][j+1]

Where first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

Time Complexity: O(s.length * p.length)
Space Complexity: O(s.length * p.length) for DP table
"""

def isMatch(s: str, p: str) -> bool:
    """
    Implement regular expression matching with support for '.' and '*'.
    
    Args:
        s: Input string
        p: Pattern string with '.' and '*' support
        
    Returns:
        True if s matches p, False otherwise
    """
    # Memoization cache
    memo = {}
    
    def dp(i: int, j: int) -> bool:
        """
        Returns True if s[i:] matches p[j:].
        """
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Base case: if we've reached the end of pattern
        if j == len(p):
            result = i == len(s)
        else:
            # Check if first characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
            # If next character is '*', handle the star
            if j + 1 < len(p) and p[j + 1] == '*':
                # Two options: 
                # 1. Skip the pattern (x* matches zero occurrences)
                # 2. Use the pattern if first character matches (x* matches one or more)
                result = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Simple case: characters must match and move to next
                result = first_match and dp(i + 1, j + 1)
        
        memo[(i, j)] = result
        return result
    
    return dp(0, 0)

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "aa"
    p1 = "a"
    result1 = isMatch(s1, p1)
    print(f"Test 1: s = '{s1}', p = '{p1}'")
    print(f"Result: {result1}")  # Expected: False
    assert result1 == False
    
    # Test case 2
    s2 = "aa"
    p2 = "a*"
    result2 = isMatch(s2, p2)
    print(f"\nTest 2: s = '{s2}', p = '{p2}'")
    print(f"Result: {result2}")  # Expected: True
    assert result2 == True
    
    # Test case 3
    s3 = "ab"
    p3 = ".*"
    result3 = isMatch(s3, p3)
    print(f"\nTest 3: s = '{s3}', p = '{p3}'")
    print(f"Result: {result3}")  # Expected: True
    assert result3 == True
    
    # Test case 4
    s4 = "aab"
    p4 = "c*a*b"
    result4 = isMatch(s4, p4)
    print(f"\nTest 4: s = '{s4}', p = '{p4}'")
    print(f"Result: {result4}")  # Expected: True
    assert result4 == True
    
    # Test case 5
    s5 = "mississippi"
    p5 = "mis*is*p*."
    result5 = isMatch(s5, p5)
    print(f"\nTest 5: s = '{s5}', p = '{p5}'")
    print(f"Result: {result5}")  # Expected: False
    assert result5 == False
    
    # Additional test cases
    s6 = ""
    p6 = "a*"
    result6 = isMatch(s6, p6)
    print(f"\nTest 6: s = '{s6}', p = '{p6}'")
    print(f"Result: {result6}")  # Expected: True
    assert result6 == True
    
    s7 = "a"
    p7 = "ab*"
    result7 = isMatch(s7, p7)
    print(f"\nTest 7: s = '{s7}', p = '{p7}'")
    print(f"Result: {result7}")  # Expected: True
    assert result7 == True
    
    s8 = "ab"
    p8 = ".*c"
    result8 = isMatch(s8, p8)
    print(f"\nTest 8: s = '{s8}', p = '{p8}'")
    print(f"Result: {result8}")  # Expected: False
    assert result8 == False
    
    print("\nAll tests passed!")