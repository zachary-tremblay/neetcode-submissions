class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hs = {i:[] for i in range(n)}

        for ed1, ed2 in edges:
            hs[ed1].append(ed2)
            hs[ed2].append(ed1)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for children in hs[node]:
                if children != parent:
                    if not dfs(children, node):
                        return False
            return True

        if not dfs(0, -1):
            return False
        
        return len(visited) == n

            