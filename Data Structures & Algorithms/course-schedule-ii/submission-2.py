class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visit = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
        result = []
        def dfs(course):
            if visit[course] == 1: return False
            if visit[course] == 2: return True
            visit[course] = 1
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            visit[course] = 2
            result.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        result.reverse()
        return result