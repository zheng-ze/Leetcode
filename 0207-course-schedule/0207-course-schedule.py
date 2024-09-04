class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses < 2 or not prerequisites:
            return True
        
        numPrereqs, prereqFor = [0 for _ in range(numCourses)], collections.defaultdict(lambda: set())
        
        for (course, prereq) in prerequisites:
            numPrereqs[course] += 1
            prereqFor[prereq].add(course)
        
        q = deque(i for i, num in enumerate(numPrereqs) if num == 0)
        
        numCompleted = 0
        while q:
            course = q.popleft()
            numCompleted += 1
            
            for c in prereqFor[course]:
                numPrereqs[c] -= 1
                
                if not numPrereqs[c]:
                    q.append(c)
        return numCompleted == numCourses
                