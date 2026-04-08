class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r = 0,0
        max_len = 0
        window = deque()
        while r < len(nums):
            if nums[r] == 0:
                window.append(r)
            if len(window) > k:
                # pop left and increment l 
                l = window.popleft() + 1
            max_len = max(max_len, r - l+1)
            r += 1
        return max_len