class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # make a MST with Kruskals algo

        # first, make sorted array with all edges .
        # only way to make edges is make each possible connection. 
        # cost, x, y
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([distance, tuple(points[i]), tuple(points[j])])
        edges.sort(key=lambda x : x[0]) # sort by cost


        # now, do kruskals algo with union find. 
        # if two nodes have same representative, then skip. 

        # parent dict, each point starts off pointing to itself
        parent = {}
        for point in points:
            point = tuple(point)
            parent[point] = point
        size = collections.defaultdict(int) # start at zero

        def find(point):
            if parent[point] != point:
                parent[point] = find(parent[point])
            return parent[point]
        
        def union(edge):
            p1, p2 = find(edge[1]), find(edge[2])

            if p1 == p2: # already connected somehow
                return False

            if size[p1] > size[p2]:
                parent[p2] = p1
                size[p1] += size[p2]
            else:
                parent[p1] = p2
                size[p2] += size[p1]
            
            return True
        
        cost = 0
        for edge in edges:
            if union(edge):
                cost += edge[0]

        return cost 


            

