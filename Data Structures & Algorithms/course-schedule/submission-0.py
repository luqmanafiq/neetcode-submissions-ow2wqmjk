class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        states = [0] * numCourses
        
        def dfs(course):
            
            if states[course] == 1: return False
            if states[course] == 2: return True
            states[course] = 1
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            states[course] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True