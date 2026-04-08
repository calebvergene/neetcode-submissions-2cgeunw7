class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ## thinking before 

        ## i need to make a dict where the keys are the hash maps
        ## of each anagram 

        ## and then the values need to be the list of words that match 
        ## with that hash map 

        final_hash = defaultdict(list)
        for word in strs:
            # get the letter freq of word
            # this method will make a hashable key (as a tuple)
            word_hash = [0]*26
            for char in word:
                word_hash[ord(char) - ord('a')] += 1
            word_hash = tuple(word_hash)
            
            # then, add it to its proper place in the final hash
            final_hash[str(word_hash)].append(word)

        # now, return the list of all of the values of the final hash. 
        # they should now be grouped based off of the frequency of their letters.
        print(final_hash)
        return list(final_hash.values()) 
