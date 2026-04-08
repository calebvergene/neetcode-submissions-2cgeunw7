class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            for other_index, other_num in enumerate(nums):
                if num + other_num == target and index != other_index:
                    return [index, other_index]