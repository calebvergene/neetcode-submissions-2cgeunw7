class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeated = []
        for i in nums:
            if i in repeated:
                return True
            else:
                repeated.append(i)
                continue
        return False