class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxi=float('-inf')
        for i,j,k in trips:
            maxi=max(maxi,k)
        trips=sorted(trips, key=lambda x: x[1])
        ct=0
        for i in range(maxi+1):
            for j,k,l in trips:
                if i==k:
                    ct+=j
                if i==l:
                    ct-=j
                if ct>capacity:
                    return False
        return True