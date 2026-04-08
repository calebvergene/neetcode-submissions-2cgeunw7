class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # so width and min height between two is the difference 
        # start on the outsides. move the pointer who has the min height. 
        # update max area each time 
        l, r = 0, len(heights)-1 

        def area(l, r):
            width = r-l
            height = min(heights[l], heights[r])
            return width * height

        max_area = area(l, r)

        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
            # update
            max_area = max(max_area, area(l,r))
        
        return max_area
