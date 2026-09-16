"""
LeetCode 17: Letter Combinations of a Phone Number
Difficulty: Medium
Topics: Hash Table, String, Backtracking

Problem:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

Approach:
Use backtracking (depth-first search) to generate all combinations.
For each digit, iterate through all possible letters it can represent,
and recursively build combinations.

Time Complexity: O(3^m * 4^n) where m is number of digits that map to 3 letters,
                 n is number of digits that map to 4 letters, and m+n = total digits
Space Complexity: O(m+n) for the recursion stack
"""

from typing import List

def letterCombinations(digits: str) -> List[str]:
    """
    Return all possible letter combinations that the number could represent.
    
    Args:
        digits: String containing digits from 2-9
        
    Returns:
        List of all possible letter combinations
    """
    if not digits:
        return []
    
    # Mapping of digits to letters (like on telephone buttons)
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(index: int, current_combination: str):
        """
        Backtracking function to build letter combinations.
        
        Args:
            index: Current digit index being processed
            current_combination: Current combination built so far
        """
        # Base case: if we've processed all digits
        if index == len(digits):
            result.append(current_combination)
            return
        
        # Get letters that current digit can represent
        current_digit = digits[index]
        possible_letters = phone_map[current_digit]
        
        # Try each possible letter
        for letter in possible_letters:
            # Add current letter and move to next digit
            backtrack(index + 1, current_combination + letter)
    
    # Start backtracking from first digit
    backtrack(0, "")
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    digits1 = "23"
    result1 = letterCombinations(digits1)
    print(f"Test 1: digits = '{digits1}'")
    print(f"Result: {sorted(result1)}")  # Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    expected1 = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert sorted(result1) == sorted(expected1)
    
    # Test case 2
    digits2 = ""
    result2 = letterCombinations(digits2)
    print(f"\nTest 2: digits = '{digits2}'")
    print(f"Result: {result2}")  # Expected: []
    assert result2 == []
    
    # Test case 3
    digits3 = "2"
    result3 = letterCombinations(digits3)
    print(f"\nTest 3: digits = '{digits3}'")
    print(f"Result: {sorted(result3)}")  # Expected: ["a","b","c"]
    expected3 = ["a","b","c"]
    assert sorted(result3) == sorted(expected3)
    
    # Additional test cases
    digits4 = "234"
    result4 = letterCombinations(digits4)
    print(f"\nTest 4: digits = '{digits4}'")
    print(f"Number of combinations: {len(result4)}")  # Expected: 3*3*3 = 27
    assert len(result4) == 27
    # Check a few combinations
    assert "adg" in result4
    assert "adz" in result4
    assert "cfh" in result4
    
    digits5 = "7"
    result5 = letterCombinations(digits5)
    print(f"\nTest 5: digits = '{digits5}'")
    print(f"Result: {sorted(result5)}")  # Expected: ["p","q","r","s"]
    expected5 = ["p","q","r","s"]
    assert sorted(result5) == sorted(expected5)
    
    print("\nAll tests passed!")