class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashnum = defaultdict(int) # make a default dict of 0s to count frequency

        for num in nums:
            hashnum[num] += 1 # increment count of int for each occurence
        
        sorted_hash = sorted(hashnum, key=lambda x: hashnum[x], reverse=True)
        
        final = []
        for index, key in enumerate(sorted_hash):
            final.append(key)

            if index >= k-1:
                return final
            

            



