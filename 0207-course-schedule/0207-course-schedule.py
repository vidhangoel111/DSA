class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        # Build directed graph
        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # 0 = Not Visited
        # 1 = Currently Exploring
        # 2 = Completely Explored
        state = [0] * numCourses

        def dfs(course):

            # Currently in the current DFS path
            # -> cycle found
            if state[course] == 1:
                return False

            # Already completely explored
            # -> no cycle from this course
            if state[course] == 2:
                return True

            # Mark as Currently Exploring
            state[course] = 1

            # Explore all dependent courses
            for next_course in graph[course]:

                if not dfs(next_course):
                    return False

            # All neighbours safely explored
            state[course] = 2

            return True

        # Graph may be disconnected,
        # so check every course
        for course in range(numCourses):

            if state[course] == 0:

                if not dfs(course):
                    return False

        return True
        
        
        
        