class Solution:
    def isValid(self, s: str) -> bool:
        hashs = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for char in s:
            ## add opening to stack
            if char in hashs.values():
                stack.append(char)
            else:
                ## if stack empty and get to closing then not valid
                if len(stack) == 0:
                    return False
                ## if top element not matching opening that not valid 
                if stack.pop() != hashs[char]:
                    return False
        return len(stack) == 0

        