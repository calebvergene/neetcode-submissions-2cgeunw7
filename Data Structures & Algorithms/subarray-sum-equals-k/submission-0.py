class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum with hash map. sort of like 2 sum. 
        prefix = defaultdict(int)
        prefix[0] = 1

        total = 0 # counts the total sum up to that index
        subarrays = 0
        for num in nums:
            total += num 
            subarrays += prefix[total - k]
            prefix[total] += 1
        return subarrays