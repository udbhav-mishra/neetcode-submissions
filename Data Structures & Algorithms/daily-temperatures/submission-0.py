class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        tstack = []
        answer = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            
            if tstack:
                while tstack and tstack[-1][0] < t:
                    prevt, prevd = tstack.pop()
                    answer[prevd] = i - prevd
            tstack.append([t, i])
        
        return answer