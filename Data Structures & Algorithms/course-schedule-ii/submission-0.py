class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topilogical sort problem, just find a valid ordering of courses
        # ALSO NEED CYCLE DETECTION

        # make adjacency list
        adj = collections.defaultdict(list)
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
        
        # init stack and visited set
        stack = [] # we return this reversed for valid order
        visited = set()
        # for each path need cycle detection
        cycle = False

        # dfs each node then when you back track, add it to the stack if it isnt already in the stack
        # this allows you to track from the end. 
        def dfs(course, path):
            # already dfs it
            if course in visited: 
                return 
            # cycle found
            if course in path:
                nonlocal cycle
                cycle = True
                return
            path.add(course)
            for nxt in adj[course]:
                dfs(nxt, path)
            # backtrack out of course, search is done with this course
            visited.add(course)
            path.remove(course)
            stack.append(course)
        
        for course in range(numCourses):
            dfs(course, set())

        return stack[::-1] if not cycle else []