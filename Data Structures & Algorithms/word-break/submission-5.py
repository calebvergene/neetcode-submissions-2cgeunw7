class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # use recursion and go through the string, kinda need to backtrack
        # with two pointers, see if you make a word. if you do, recursive call the string excluding that word.
        # use memoization to store index pairs that form a word. 

        wordDict = set(wordDict)
        # memoiz will return start indexes that failed
        memoiz = set()

        def dp(start):
            # basecase, if we reach end of string successfully
            if start == len(s):
                return True

            # word with starting index already parsed and stored, we know they didnt work
            if start in memoiz:
                return False
                
            # not already parsed, iterate index until you find a word
            for index in range(start+1, len(s)+1):
                if s[start:index] in wordDict:
                    # if word is found, recursive call next part of the string with the already found word
                    if dp(index):
                        return True
                # if recursive call returns false, keep going. 

            # if not true after the for loop, return false. 
            memoiz.add(start)
            return False
        return dp(0)

