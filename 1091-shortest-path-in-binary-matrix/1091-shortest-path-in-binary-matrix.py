from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        q = deque()

        visited = [[False] * n for _ in range(n)]
        q.append((0,0,1))
        visited[0][0] = True

        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        while q:
            row, col, distance = q.popleft()

            if row == n - 1 and col == n - 1:
                return distance
            
            for dr,dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (0 <= new_row < n and
                    0 <= new_col < n and
                    grid[new_row][new_col] == 0 and
                    not visited[new_row][new_col]):
                    visited[new_row][new_col] = True
                    q.append((new_row, new_col, distance + 1))
        return -1           

