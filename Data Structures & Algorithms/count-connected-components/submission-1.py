class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hs = {i:[] for i in range(n)}

        for a, b in edges:
            hs[a].append(b)
            hs[b].append(a)

        res = 0
        seen = set()
        current = set()
        def dfs(node, parent):
            if node in seen:
                return
            seen.add(node)

            for neighbour in hs[node]:
                if neighbour != parent:
                    dfs(neighbour, node)
            
        for i in range(n):
            if i not in seen:
                res += 1
            dfs(i, -1)
        return res
            