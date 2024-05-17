"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


from pythainlp.util import num_to_thaiword

class Solution:
    def __init__(self, number: int):
        self.number = number

    def number_to_thai(self) -> str:
        result = ''
        if self.number >= 0:
            result = num_to_thaiword(self.number)
            
        else: 
            result = 'number can not less than 0'
        
        return result


input = 101
output = Solution(input)
output = output.number_to_thai()
print("number_to_thai: ", output)