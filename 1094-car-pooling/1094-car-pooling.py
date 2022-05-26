class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxi = 0
        for i,j,k in trips:
            maxi = max(k,maxi)
        sol = [0 for i in range(maxi+1)]
        for i,j,k in trips:
            if i>capacity:
                return False
            sol[j]+=i
            sol[k]-=i
        for i in range(1,len(sol)):
            sol[i] += sol[i-1]
            if sol[i] > capacity:
                return False
        return True