"""
LeetCode 5: Longest Palindromic Substring
Difficulty: Medium
Topics: String, Dynamic Programming

Problem:
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.

Approach:
Expand around center technique. For each character in the string, treat it as the center
of a potential palindrome and expand outwards as long as the characters match.
We need to check both odd-length and even-length palindromes.

Time Complexity: O(n^2) where n is the length of the string.
Space Complexity: O(1) - Only using constant extra space.
"""

def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    
    Args:
        s: Input string
        
    Returns:
        The longest palindromic substring
    """
    if not s:
        return ""
    
    start = 0
    end = 0
    
    def expand_around_center(left: int, right: int) -> int:
        """
        Expand around the center and return the length of the palindrome.
        
        Args:
            left: Left index
            right: Right index
            
        Returns:
            Length of the palindrome found
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(s)):
        # Check for odd-length palindromes (center is at i)
        len1 = expand_around_center(i, i)
        # Check for even-length palindromes (center is between i and i+1)
        len2 = expand_around_center(i, i + 1)
        
        # Take the maximum length
        max_len = max(len1, len2)
        
        # If we found a longer palindrome, update start and end
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end + 1]

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "babad"
    result1 = longest_palindromic_substring(s1)
    print(f"Test 1: s = '{s1}'")
    print(f"Result: '{result1}'")  # Expected: "bab" or "aba"
    assert result1 in ["bab", "aba"]
    
    # Test case 2
    s2 = "cbbd"
    result2 = longest_palindromic_substring(s2)
    print(f"\nTest 2: s = '{s2}'")
    print(f"Result: '{result2}'")  # Expected: "bb"
    assert result2 == "bb"
    
    # Test case 3
    s3 = "a"
    result3 = longest_palindromic_substring(s3)
    print(f"\nTest 3: s = '{s3}'")
    print(f"Result: '{result3}'")  # Expected: "a"
    assert result3 == "a"
    
    # Test case 4
    s4 = "ac"
    result4 = longest_palindromic_substring(s4)
    print(f"\nTest 4: s = '{s4}'")
    print(f"Result: '{result4}'")  # Expected: "a" or "c"
    assert result4 in ["a", "c"]
    
    # Test case 5
    s5 = "forgeeksskeegfor"
    result5 = longest_palindromic_substring(s5)
    print(f"\nTest 5: s = '{s5}'")
    print(f"Result: '{result5}'")  # Expected: "geeksskeeg"
    assert result5 == "geeksskeeg"
    
    print("\nAll tests passed!")