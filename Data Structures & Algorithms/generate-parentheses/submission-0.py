class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # pass in two lists: 
        # one to add to output and another as validation stack.
        output = []
        chars = ['(', ')']
        def backtrack(current, stack):
            # track balance: if ( more than n times, we know that not possible
            if len(stack) > n:
                return

            # max amount of chars for n
            if len(current) == n*2:
                # requirements for current meet
                if not stack:
                    output.append(current)
                return
            
            for char in chars:
                # to track valid parenthesis
                if char == '(':
                    stack.append('(')
                else:
                    if stack:
                        stack.pop()
                    else:
                        return
                # backtrack
                current += char
                backtrack(current, stack)
                current = current[:-1]
                if char == '(':
                    stack.pop()
                else:
                    stack.append('(')
        backtrack("",[])
        return output 


            
