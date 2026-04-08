class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)

        def anagram(s):
            lst = [0]*26
            for char in s:
                lst[ord('a')-ord(char)] += 1
            return tuple(lst)
        
        for s in strs:
            anagram_list = anagram(s)
            group_anagrams[anagram_list].append(s)
        return list(group_anagrams.values())
