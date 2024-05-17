"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""

import roman

class Solution:

    def __init__(self, number: int):
        self.number = number

    def number_to_roman(self) -> str:
        roman_number = ''

        if self.number >= 0:
            roman_number = roman.toRoman(self.number)
        else:
            roman_number = 'number can not less than 0'

        return roman_number


input = -10
output = Solution(input)
output = output.number_to_roman()
print("number_to_roman :", output)