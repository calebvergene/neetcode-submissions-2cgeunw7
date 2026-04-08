class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        # carry will be at most 1 each time 
        # iterate and add each bit 
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            # get last digit
            aa, bb = int(a[i]) if i < len(a) else 0, int(b[i]) if i < len(b) else 0
            # now add with carry. either 0, 1, 2, 3
            toadd = aa + bb + carry
            carry = toadd // 2
            toadd = toadd % 2
            
            # add to res 
            res = str(toadd) + res
        
        if carry:
            res = "1" + res
        return res

