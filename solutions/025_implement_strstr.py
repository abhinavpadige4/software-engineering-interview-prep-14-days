"""
LeetCode 28: Implement strStr()
Difficulty: Easy
Topics: String, Two Pointers, String Matching

Problem:
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. 
This is consistent with C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2
Explanation: The substring "ll" starts at index 2 in "hello".

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
Explanation: The substring "bba" is not part of "aaaaa".

Example 3:
Input: haystack = "", needle = ""
Output: 0
Explanation: Both strings are empty, so we return 0.

Constraints:
- 0 <= haystack.length, needle.length <= 5 * 10^4
- haystack and needle consist of only lowercase English characters.

Approach:
Simple sliding window approach:
1. Handle edge case: if needle is empty, return 0
2. If needle is longer than haystack, return -1
3. Slide a window of size len(needle) over haystack
4. Check if substring at each position matches needle
5. Return first match index, or -1 if no match found

Time Complexity: O((n-m+1)*m) where n is haystack length, m is needle length
Space Complexity: O(1) - Constant extra space
"""

def strStr(haystack: str, needle: str) -> int:
    """
    Implement strStr() - find first occurrence of needle in haystack.
    
    Args:
        haystack: String to search in
        needle: String to search for
        
    Returns:
        Index of first occurrence of needle in haystack, or -1 if not found
    """
    # Handle edge cases
    if not needle:
        return 0
    
    if not haystack or len(needle) > len(haystack):
        return -1
    
    # Slide window of size len(needle) over haystack
    for i in range(len(haystack) - len(needle) + 1):
        # Check if substring matches needle
        if haystack[i:i+len(needle)] == needle:
            return i
    
    return -1

# Test cases
if __name__ == "__main__":
    # Test case 1
    haystack1 = "hello"
    needle1 = "ll"
    result1 = strStr(haystack1, needle1)
    print(f"Test 1: haystack = '{haystack1}', needle = '{needle1}'")
    print(f"Result: {result1}")  # Expected: 2
    assert result1 == 2
    
    # Test case 2
    haystack2 = "aaaaa"
    needle2 = "bba"
    result2 = strStr(haystack2, needle2)
    print(f"\nTest 2: haystack = '{haystack2}', needle = '{needle2}'")
    print(f"Result: {result2}")  # Expected: -1
    assert result2 == -1
    
    # Test case 3
    haystack3 = ""
    needle3 = ""
    result3 = strStr(haystack3, needle3)
    print(f"\nTest 3: haystack = '{haystack3}', needle = '{needle3}'")
    print(f"Result: {result3}")  # Expected: 0
    assert result3 == 0
    
    # Additional test cases
    haystack4 = "mississippi"
    needle4 = "issip"
    result4 = strStr(haystack4, needle4)
    print(f"\nTest 4: haystack = '{haystack4}', needle = '{needle4}'")
    print(f"Result: {result4}")  # Expected: 4
    assert result4 == 4
    
    haystack5 = "abc"
    needle5 = "c"
    result5 = strStr(haystack5, needle5)
    print(f"\nTest 5: haystack = '{haystack5}', needle = '{needle5}'")
    print(f"Result: {result5}")  # Expected: 2
    assert result5 == 2
    
    haystack6 = "abc"
    needle6 = "d"
    result6 = strStr(haystack6, needle6)
    print(f"\nTest 6: haystack = '{haystack6}', needle = '{needle6}'")
    print(f"Result: {result6}")  # Expected: -1
    assert result6 == -1
    
    haystack7 = "a"
    needle7 = "a"
    result7 = strStr(haystack7, needle7)
    print(f"\nTest 7: haystack = '{haystack7}', needle = '{needle7}'")
    print(f"Result: {result7}")  # Expected: 0
    assert result7 == 0
    
    haystack8 = "aaa"
    needle8 = "aaaa"
    result8 = strStr(haystack8, needle8)
    print(f"\nTest 8: haystack = '{haystack8}', needle = '{needle8}'")
    print(f"Result: {result8}")  # Expected: -1 (needle longer than haystack)
    assert result8 == -1
    
    print("\nAll tests passed!")