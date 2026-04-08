class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashA = {}
        for word in strs:
            hashA.setdefault(str(sorted(word)), []).append(word)

        final = []
        for lst in hashA.values():
            final.append(lst)
        return final