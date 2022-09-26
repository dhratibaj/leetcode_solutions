class Graph:
    def __init__(self, equations):
        self.graph = self.buildGraph(equations)

    def buildGraph(self, equations):
        graph = dict()
        
        for equation in equations:
            x, y, relation = equation[0], equation[3], equation[1]
            if x not in graph:
                graph[x] = set()
            if y not in graph:
                graph[y] = set()
            if relation == '=':
                graph[x].add(y)
                graph[y].add(x)

        return graph
    
    def isEqual(self, start, end, seen = set()):
        queue = deque([start])
        seen = {start}
        
        while queue:
            node = queue.popleft()
            if node == end:
                return True
            for nextNode in self.graph[node]:
                if nextNode not in seen:
                    queue.append(nextNode)
                    seen.add(nextNode)
            
        return False

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = Graph(equations)

        for equation in equations:
            x, y, relation = equation[0], equation[3], equation[1]
            if relation == '!' and graph.isEqual(x, y):
                return False
            if relation == '=' and not graph.isEqual(x, y):
                return False

        return True