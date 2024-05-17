"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""

from typing import Union

class Solution:

    def __init__(self, number: int) -> None:
        self.number = number

    def find_tailing_zeroes(self) -> Union[int, str]:
        count = 0
        i = 5

        if self.number >= 0:
            while (self.number / i >= 1):
                count += int(self.number / i)
                i *= 5
        else:
            count = "number can not be negative"

        return count
    
n = 25
res = Solution(n)
result = res.find_tailing_zeroes()

print("find_tailing_zeroes: ", result)

