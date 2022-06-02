class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lastRain = {}
        dryDays = []
        ans = [1] * len(rains)
        for i in range(len(rains)):
            if rains[i] == 0:
                dryDays.append(i)
            else:
                if rains[i] in lastRain:
                    flag = 0
                    for j in dryDays:
                        if j>lastRain[rains[i]]:
                            ans[j] = rains[i]
                            dryDays.remove(j)
                            flag = 1
                            break
                    if flag == 0:
                        return []
                    lastRain[rains[i]] = i
                else:
                    lastRain[rains[i]] = i
                ans[i] = -1
        return ans