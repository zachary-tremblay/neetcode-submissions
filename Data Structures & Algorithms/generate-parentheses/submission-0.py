class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def dfs(opn, cls):
            if cls > opn or len(curr) > 2*n:
                return
            if len(curr) == 2*n and cls == opn:
                res.append("".join(curr.copy()))
                return
            
            curr.append('(')
            dfs(opn+1, cls)
            curr.pop()

            curr.append(')')
            dfs(opn, cls+1)
            curr.pop()

        dfs(0, 0)
        return res