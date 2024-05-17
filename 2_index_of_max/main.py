"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 4

[Example 2]
input = []
output = list can not blank
"""

from typing import Union

class Solution:

    def __init__(self, listNumber: list):
        self.numbers = listNumber

    def find_max_index(self) -> Union[int, str]:
        result = 0

        if len(self.numbers) > 0:
            prepare_list = []
            [prepare_list.append(x) for x in self.numbers if x not in prepare_list]
            result = prepare_list.index(max(prepare_list))
        else:
            result = "list can not blank"

        return result

input = [1,2,1,3,5,6,4]
# input = []
res = Solution(input)
output = res.find_max_index()
print("find_max_index: ", output)