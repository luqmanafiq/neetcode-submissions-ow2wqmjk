class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # check if i < i+1
        # append 1
        # if not pop and increment its position by 1
        result = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        return result