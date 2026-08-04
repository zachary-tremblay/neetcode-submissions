class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hs = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            hs[course].append(prereq)
        
        visited = set()
        completed = set()
        res = []
        def dfs(course):
            if course in visited:
                return False
            if course in completed:
                return True
            visited.add(course)
            for prereq in hs[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            completed.add(course)
            res.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

