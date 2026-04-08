class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                repeated = ""
                print(stack)
                while stack[-1] != "[":
                    part = stack.pop()
                    for i in range(len(part)-1, -1, -1):
                        repeated += part[i]
                repeated = repeated[::-1]
                stack.pop()
                num = ""
                while stack and stack[-1].isnumeric():
                    num += stack.pop()
                num = int(num[::-1])
                repeated *= num
                stack += repeated.split()
                continue
            stack.append(char)
        return "".join(stack)
