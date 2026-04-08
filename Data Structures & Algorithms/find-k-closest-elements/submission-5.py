class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary search to find the closest element
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        
        # Now left points to the first element >= x
        # Find the closest element to x
        if left > 0 and (left == len(arr) or abs(arr[left-1] - x) <= abs(arr[left] - x)):
            left -= 1
        
        # Set initial window
        l = r = left
        
        # Expand window to include k elements
        while r - l + 1 < k:
            if l == 0:
                r += 1
            elif r == len(arr) - 1:
                l -= 1
            elif abs(arr[l-1] - x) <= abs(arr[r+1] - x):
                l -= 1
            else:
                r += 1
        
        return arr[l:r+1]