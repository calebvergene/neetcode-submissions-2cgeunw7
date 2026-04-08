class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        ## create a hashmap with default 0 
        hashnums = defaultdict(int)

        ## count frequency of each number 
        for num in nums: 
            hashnums[num] += 1
        
        ## sort the dictionary
        sorteddict = dict(sorted(hashnums.items(), key= lambda item:item[1], reverse=True))
        listk = []
        sortedkeys = list(sorteddict.keys())
        
        ## add the first k elements of the sorted dict
        for i in range(k):
            listk.append(sortedkeys[i])
        
        return listk


        




