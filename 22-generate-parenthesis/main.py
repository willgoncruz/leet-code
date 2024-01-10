class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(s: str, left: int, right: int, res: List[str]):
            if len(s) == 2 * n:
                res.append(s)
                return
            
            if left < n:
                dfs(s + "(", left + 1, right, res)
            
            if right < left:
                dfs(s + ")", left, right + 1, res)

        res = []
        dfs("", 0, 0, res)
        return res
