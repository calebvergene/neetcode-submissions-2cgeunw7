class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        total_length = sum(matchsticks)
        length = total_length // 4
        if total_length % 4 != 0 or max(matchsticks) > length:
            return False
        
        def backtrack(side, remaining, sides_formed, length):
            if side == length:
                side = 0
                sides_formed += 1
            if side > length: # if side > length, then return because bad path
                return False
            if sides_formed == 4 and len(remaining) == 0:
                return True
            
            for m in range(len(remaining)):
                # if side hits length exactly, then increment sides formed
                side += remaining[m]
                square = backtrack(side, remaining[:m]+remaining[m+1:], sides_formed, length)
                side -= remaining[m]
                if square == True:
                    return True
                if side == 0:
                    return False
            return False
                
        return backtrack(0, sorted(matchsticks, reverse=True), 0, length)




            

            
        
        