class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0
        while r > l: 
            # minimum height the wall needs to be for efficiency
            if max_area / len(heights) > min(heights[l], heights[r]):
                if heights[r] < heights[l]:
                    r -= 1
                else:
                    l += 1
                continue

            # see if dimensions of wall and distance would be max height 
            res = (min(heights[l], heights[r]) * (r - l))
            if res > max_area:
                max_area = res
            
            # now, increment the side with the smaller wall
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return max_area
            
        