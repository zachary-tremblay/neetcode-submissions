class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        l = len(edges)
        par = [i for i in range(l+1)]

        def find(n):
            if par[n] != n:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            par[p2] = p1
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]

            
        
