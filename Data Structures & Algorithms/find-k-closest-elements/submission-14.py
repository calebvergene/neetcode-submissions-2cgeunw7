class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # need to binary search to find closest index to x
        l, r = 1, len(arr)-2
        while l <= r:
            mid = (l+r)//2
            print(mid, l, r)
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        
        # set r and l to the closest one to x 
        if l > 0 and (abs(arr[l-1]-x) <= abs(arr[l]-x)):
            l -= 1
        r = l
        # then two pointer out finding the k closest ints to x
        while (r-l+1)< k:
            if l == 0:
                r += 1
            elif r == len(arr) - 1:
                l -= 1
            elif abs(arr[l-1]-x) <= abs(arr[r+1]-x):
                l -= 1
            else:
                r+= 1
        
        return arr[l:r+1]