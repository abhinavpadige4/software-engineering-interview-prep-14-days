"""
LeetCode 6: Zigzag Conversion
Difficulty: Medium
Topics: String

Problem:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I   S

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
- 1 <= s.length <= 1000
- 1 <= numRows <= 1000

Approach:
Simulate the zigzag pattern by placing characters in the appropriate rows.
We move down the rows until we hit the bottom, then move up until we hit the top,
repeating this pattern. Each character goes to the current row based on our direction.

Time Complexity: O(n) where n is the length of the string.
Space Complexity: O(n) for storing the rows.
"""

def convert(s: str, numRows: int) -> str:
    """
    Convert a string to zigzag pattern and read line by line.
    
    Args:
        s: Input string
        numRows: Number of rows in the zigzag pattern
        
    Returns:
        String read line by line from the zigzag pattern
    """
    # If only one row or string is shorter than numRows, return as-is
    if numRows == 1 or numRows >= len(s):
        return s
    
    # Create rows to store characters
    rows = [''] * min(numRows, len(s))
    current_row = 0
    going_down = False
    
    # Place each character in the appropriate row
    for char in s:
        rows[current_row] += char
        
        # Change direction if we hit top or bottom
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        
        # Move to next row
        current_row += 1 if going_down else -1
    
    # Join all rows
    return ''.join(rows)

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    result1 = convert(s1, numRows1)
    print(f"Test 1: s = '{s1}', numRows = {numRows1}")
    print(f"Result: '{result1}'")  # Expected: "PAHNAPLSIIGYIR"
    assert result1 == "PAHNAPLSIIGYIR"
    
    # Test case 2
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    result2 = convert(s2, numRows2)
    print(f"\nTest 2: s = '{s2}', numRows = {numRows2}")
    print(f"Result: '{result2}'")  # Expected: "PINALSIGYAHRPI"
    assert result2 == "PINALSIGYAHRPI"
    
    # Test case 3
    s3 = "A"
    numRows3 = 1
    result3 = convert(s3, numRows3)
    print(f"\nTest 3: s = '{s3}', numRows = {numRows3}")
    print(f"Result: '{result3}'")  # Expected: "A"
    assert result3 == "A"
    
    # Additional test cases
    s4 = "AB"
    numRows4 = 1
    result4 = convert(s4, numRows4)
    print(f"\nTest 4: s = '{s4}', numRows = {numRows4}")
    print(f"Result: '{result4}'")  # Expected: "AB"
    assert result4 == "AB"
    
    s5 = "ABCD"
    numRows5 = 2
    result5 = convert(s5, numRows5)
    print(f"\nTest 5: s = '{s5}', numRows = {numRows5}")
    print(f"Result: '{result5}'")  # Expected: "ACBD"
    assert result5 == "ACBD"
    
    print("\nAll tests passed!")