class Solution:
    def reorganizeString(self, s: str) -> str:
        # trick is that you want the highest freq characters to be placed first 
        res = ""
        
        # get freqs
        freq = collections.defaultdict(int)
        for char in s:
            freq[char] += 1
        
        heap = [[-freq[char], char] for char in freq]
        heapq.heapify(heap)

        cooldown = None

        while heap:
            nxt = heapq.heappop(heap)
            if cooldown:
                heapq.heappush(heap, cooldown)
                cooldown = None
            res += nxt[1]
            nxt[0] += 1
            if nxt[0]:
                # then eventually add back to heap
                cooldown = nxt



        # if final string is less than og, return ""
        return "" if len(res) < len(s) else res