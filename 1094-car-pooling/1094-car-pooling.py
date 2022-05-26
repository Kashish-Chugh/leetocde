class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxi = 0
        for i,j,k in trips:
            maxi = max(k,maxi)
        sol = [0 for i in range(maxi+1)]
        for i,j,k in trips:
            sol[j]+=i
            sol[k]-=i
        prev = sol[0]
        if prev>capacity:
            return False
        for i in sol[1:]:
            prev += i
            if prev > capacity:
                return False
        return True