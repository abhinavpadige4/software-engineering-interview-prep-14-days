"""
LeetCode 3: Longest Substring Without Repeating Characters
Difficulty: Medium
Topics: Hash Table, String, Sliding Window

Problem:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

Approach:
Use sliding window technique with a hash map to track the last seen index of each character.
Expand the window by moving the right pointer, and when we encounter a duplicate,
move the left pointer to the position right after the last occurrence of that character.

Time Complexity: O(n) where n is the length of the string.
Space Complexity: O(min(m, n)) where m is the size of the charset.
"""

def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring without repeating characters
    """
    # Hash map to store the last index where each character was seen
    char_index_map = {}
    max_length = 0
    left = 0  # Left pointer of the sliding window
    
    for right in range(len(s)):
        current_char = s[right]
        
        # If the character is already in the current window,
        # move the left pointer to the right of the last occurrence
        if current_char in char_index_map and char_index_map[current_char] >= left:
            left = char_index_map[current_char] + 1
        
        # Update the last seen index of the current character
        char_index_map[current_char] = right
        
        # Update max length
        current_length = right - left + 1
        max_length = max(max_length, current_length)
    
    return max_length

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "abcabcbb"
    result1 = length_of_longest_substring(s1)
    print(f"Test 1: s = '{s1}'")
    print(f"Result: {result1}")  # Expected: 3
    assert result1 == 3
    
    # Test case 2
    s2 = "bbbbb"
    result2 = length_of_longest_substring(s2)
    print(f"\nTest 2: s = '{s2}'")
    print(f"Result: {result2}")  # Expected: 1
    assert result2 == 1
    
    # Test case 3
    s3 = "pwwkew"
    result3 = length_of_longest_substring(s3)
    print(f"\nTest 3: s = '{s3}'")
    print(f"Result: {result3}")  # Expected: 3
    assert result3 == 3
    
    # Additional test cases
    s4 = ""
    result4 = length_of_longest_substring(s4)
    print(f"\nTest 4: s = '{s4}' (empty string)")
    print(f"Result: {result4}")  # Expected: 0
    assert result4 == 0
    
    s5 = "abcdef"
    result5 = length_of_longest_substring(s5)
    print(f"\nTest 5: s = '{s5}'")
    print(f"Result: {result5}")  # Expected: 6
    assert result5 == 6
    
    print("\nAll tests passed!")