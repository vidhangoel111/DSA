from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # Create adjacency list
        graph = [[] for _ in range(numCourses)]

        # Indegree = number of prerequisites for each course
        indegree = [0] * numCourses

        # Build the graph
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        # Add courses with no prerequisites
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Process courses
        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        # If all courses were completed, there is no cycle
        return completed == numCourses