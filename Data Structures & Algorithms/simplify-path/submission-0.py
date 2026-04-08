class Solution:
    def simplifyPath(self, path: str) -> str:
        # use a stack to simulate the levels of the path
        stack = []
        curr = "/"
        path += "/"

        for char in path:
            # skip if double slash
            if char == "/" and curr[-1] == "/":
                continue
            # new part of path. add the one we finished. 
            elif char == "/":
                # check for periods
                if curr == "/..":
                    if stack: stack.pop()
                # here we should be good. so now add. 
                elif curr != "/.":
                    stack.append(curr)
                curr = "/"
            else:
                curr += char
        if not stack:
            return "/"
        return "".join(stack)