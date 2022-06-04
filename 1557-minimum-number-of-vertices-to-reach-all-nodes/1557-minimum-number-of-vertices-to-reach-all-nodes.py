class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        sol = [0] * n
        ans = []
        for i in edges:
            sol[i[1]] +=1
        for i in range(len(sol)):
            if sol[i] == 0:
                ans.append(i)
        return ans
