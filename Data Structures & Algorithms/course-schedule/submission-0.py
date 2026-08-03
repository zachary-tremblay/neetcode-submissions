class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hs = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            hs[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if len(hs[course]) == 0:
                return True
            visited.add(course)
            for prereq in hs[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            hs[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
