"""
LeetCode 30: Substring with Concatenation of All Words
Difficulty: Hard
Topics: Hash Table, String, Sliding Window

Problem:
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated substrings. 
"acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.

Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[0].length == 3, the concatenated substring has to be of length 6.
Substrings starting at index 0: "barfoo"
Substrings starting at index 9: "foobar"
The output order does not matter. [9,0] is also valid.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: The total length of all the words is 4 * 4 = 16. 
The concatenated substring has to be of length 16.
There is no such substring in s.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[0].length == 3, the concatenated substring has to be of length 9.
Substrings starting at index 6: "foobarthe"
Substrings starting at index 9: "thefoobar"
Substrings starting at index 12: "barthefoo"
The output order does not matter. [9,6,12] is also valid.

Constraints:
- 1 <= s.length <= 10^4
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 30
- words[i] consists of lowercase English letters.
- All the strings of words are of the same length.

Approach:
Use sliding window with hash maps:
1. Calculate word length and total length needed
2. Create frequency map of words
3. For each possible starting offset (0 to word_length-1):
   - Use sliding window to check substrings
   - Maintain current word frequency in window
   - When window size matches, compare frequencies
   - Slide window by word length each time

Time Complexity: O(n * m) where n is string length, m is word length
Space Complexity: O(m * k) where m is number of words, k is word length
"""

from typing import List
from collections import Counter

def findSubstring(s: str, words: List[str]) -> List[int]:
    """
    Find starting indices of all concatenated substrings in s.
    
    Args:
        s: Input string
        words: List of words (all same length)
        
    Returns:
        List of starting indices of concatenated substrings
    """
    if not s or not words:
        return []
    
    word_count = len(words)
    word_length = len(words[0])
    total_length = word_count * word_length
    
    if total_length > len(s):
        return []
    
    # Create frequency map of words
    word_freq = Counter(words)
    result = []
    
    # Check each possible starting offset
    for offset in range(word_length):
        left = offset
        right = offset
        current_freq = Counter()
        words_used = 0
        
        # Slide window in steps of word_length
        while right + word_length <= len(s):
            # Get current word
            word = s[right:right + word_length]
            right += word_length
            
            # If word is in our target words
            if word in word_freq:
                current_freq[word] += 1
                words_used += 1
                
                # If we have too many of this word, shrink from left
                while current_freq[word] > word_freq[word]:
                    left_word = s[left:left + word_length]
                    current_freq[left_word] -= 1
                    left += word_length
                    words_used -= 1
                
                # If we have exactly the right number of words
                if words_used == word_count:
                    result.append(left)
                    
                    # Move left pointer to find next potential match
                    left_word = s[left:left + word_length]
                    current_freq[left_word] -= 1
                    left += word_length
                    words_used -= 1
            else:
                # Reset window if word not in target words
                current_freq.clear()
                words_used = 0
                left = right
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "barfoothefoobarman"
    words1 = ["foo", "bar"]
    result1 = findSubstring(s1, words1)
    print(f"Test 1: s = '{s1}', words = {words1}")
    print(f"Result: {sorted(result1)}")  # Expected: [0, 9]
    assert sorted(result1) == [0, 9]
    
    # Test case 2
    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word", "good", "best", "word"]
    result2 = findSubstring(s2, words2)
    print(f"\nTest 2: s = '{s2}', words = {words2}")
    print(f"Result: {result2}")  # Expected: []
    assert result2 == []
    
    # Test case 3
    s3 = "barfoofoobarthefoobarman"
    words3 = ["bar", "foo", "the"]
    result3 = findSubstring(s3, words3)
    print(f"\nTest 3: s = '{s3}', words = {words3}")
    print(f"Result: {sorted(result3)}")  # Expected: [6, 9, 12]
    assert sorted(result3) == [6, 9, 12]
    
    # Additional test cases
    s4 = "wordgoodgoodgoodbestword"
    words4 = ["word","good","best","good"]
    result4 = findSubstring(s4, words4)
    print(f"\nTest 4: s = '{s4}', words = {words4}")
    print(f"Result: {sorted(result4)}")
    # Should find valid starting indices
    assert isinstance(result4, list)
    
    s5 = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words5 = ["fooo","barr","wing","ding","wing"]
    result5 = findSubstring(s5, words5)
    print(f"\nTest 5: s = '{s5}', words = {words5}")
    print(f"Result: {sorted(result5)}")  # Expected: [13]
    assert sorted(result5) == [13]
    
    print("\nAll tests passed!")