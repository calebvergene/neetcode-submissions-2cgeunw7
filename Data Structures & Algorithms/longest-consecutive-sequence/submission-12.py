class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = collections.defaultdict(int)
        res = 0
        for num in nums:
            if num - 1 in seq:
                seq[num] = seq[num-1] + 1
            else:
                seq[num] = 1
            # from here, we have the value of num elements before it 
            # have to account for elemetns that are after num too
            ahead = 1
            while num + ahead in seq:
                seq[num+ahead] = seq[num+ahead-1] + 1
                ahead += 1
            res = max(seq[num + ahead - 1], res)
        return res