class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sums = set()
        candidates.sort()
        def backtrack_sum(current, list_sum, candidates):
            # base case
            if list_sum == target:
                sums.add(tuple(current[:]))
                return
            elif list_sum > target:
                return

            for i in range(len(candidates)):
                current.append(candidates[i])
                list_sum += candidates[i]
                # so that you dont have sums with the same frequency.
                # it doesnt go back over the same combinations.
                print(current)
                backtrack_sum(current, list_sum, candidates[i+1:])
                sub = current.pop()
                list_sum -= sub
        backtrack_sum([], 0, candidates)
        return [list(s) for s in sums]