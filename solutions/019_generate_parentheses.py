"""
LeetCode 22: Generate Parentheses
Difficulty: Medium
Topics: String, Backtracking

Problem:
Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
- 1 <= n <= 8

Approach:
Use backtracking to generate all valid combinations.
At each step, we can add an opening bracket if we haven't used all n opening brackets.
We can add a closing bracket only if it wouldn't make the sequence invalid 
(i.e., number of closing brackets used < number of opening brackets used).

Time Complexity: O(4^n / sqrt(n)) - This is the nth Catalan number
Space Complexity: O(4^n / sqrt(n)) to store all combinations
"""

from typing import List

def generateParenthesis(n: int) -> List[str]:
    """
    Generate all combinations of well-formed parentheses.
    
    Args:
        n: Number of pairs of parentheses
        
    Returns:
        List of all valid combinations of parentheses
    """
    result = []
    
    def backtrack(current: str, open_count: int, close_count: int):
        """
        Backtracking function to generate parentheses combinations.
        
        Args:
            current: Current string being built
            open_count: Number of opening brackets used so far
            close_count: Number of closing brackets used so far
        """
        # Base case: if we've used all brackets
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # If we can still add an opening bracket
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        
        # If we can add a closing bracket (must not exceed opening brackets)
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)
    
    # Start with empty string and zero counts
    backtrack("", 0, 0)
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    n1 = 3
    result1 = generateParenthesis(n1)
    print(f"Test 1: n = {n1}")
    print(f"Result: {sorted(result1)}")  # Expected: ["((()))","(()())","(())()","()(())","()()()"]
    expected1 = ["((()))","(()())","(())()","()(())","()()()"]
    assert sorted(result1) == sorted(expected1)
    
    # Test case 2
    n2 = 1
    result2 = generateParenthesis(n2)
    print(f"\nTest 2: n = {n2}")
    print(f"Result: {result2}")  # Expected: ["()"]
    assert result2 == ["()"]
    
    # Test case 3
    n3 = 2
    result3 = generateParenthesis(n3)
    print(f"\nTest 3: n = {n3}")
    print(f"Result: {sorted(result3)}")  # Expected: ["(())","()()"]
    expected3 = ["(())","()()"]
    assert sorted(result3) == sorted(expected3)
    
    # Additional test cases
    n4 = 0
    result4 = generateParenthesis(n4)
    print(f"\nTest 4: n = {n4}")
    print(f"Result: {result4}")  # Expected: []
    assert result4 == []
    
    n5 = 4
    result5 = generateParenthesis(n5)
    print(f"\nTest 5: n = {n5}")
    print(f"Number of combinations: {len(result5)}")  # Expected: 14 (4th Catalan number)
    assert len(result5) == 14
    # Check that all are valid length
    for combo in result5:
        assert len(combo) == 2 * n5  # 8 characters
        # Basic validation: should start with '(' and end with ')'
        assert combo.startswith('(') and combo.endswith(')')
    
    print("\nAll tests passed!")