class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tot = [-1 for i in range(capacity)]
        trips = sorted(trips, key=lambda x: x[1])
        for j in trips:
            p = j[0]
            s = j[1]
            e = j[2]
            temp = 0
            for i in range(len(tot)):
                if tot[i] <= s:
                    tot[i] = -1
                if tot[i] == -1 and temp < p:
                    tot[i] = e
                    temp += 1
                if temp == p:
                    break
            if temp != p:
                return False
        return True
                
                