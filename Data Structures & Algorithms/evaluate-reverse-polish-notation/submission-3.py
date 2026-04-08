class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opps = ['+', '-', '*', '/']
        def solve(num1, num2, opp):
            if opp == "+":
                return num1 + num2
            elif opp == "-":
                return num2 - num1
            elif opp == "*":
                return num1 * num2
            else:
                return num2/num1
            
        ## so, i need to use a stack to pull the 2 most recent nums
        ## when i get to an opp, then solve those two funcs
        ## then add it back to the stack
        ## then the final element in the stack is the answer

        num_stack = []
        for token in tokens:
            if token in opps:
                ## pops top two elements and calls it in solve func
                answer = solve(int(num_stack.pop()), int(num_stack.pop()), token)
                num_stack.append(answer)
            else:
                num_stack.append(token)
            print(num_stack)
        return int(num_stack[-1])