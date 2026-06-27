class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)


        for i, n in enumerate(temperatures):
            
            if stack:
                while (len(stack)> 0 and n > stack[-1][0]):
                    output[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()

                stack.append((n , i))
            else:
                stack.append((n , i))
        return output