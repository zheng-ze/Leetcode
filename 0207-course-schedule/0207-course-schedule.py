class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses < 2 or not prerequisites:
            return True
        
        prereqs, prereqFor = {}, {}
        
        for i in range(numCourses):
            prereqs[i] = set()
            prereqFor[i] = set()
        
        for (course, prereq) in prerequisites:
            prereqs[course].add(prereq)
            prereqFor[prereq].add(course)
        q = deque([])
        
        for course in prereqs:
            if prereqs[course]:
                continue
            q.append(course)
        
        numCompleted = 0
        while q:
            course = q.popleft()
            numCompleted += 1
            
            for c in prereqFor[course]:
                prereqs[c].remove(course)
                
                if not prereqs[c]:
                    q.append(c)
        return numCompleted == numCourses
                