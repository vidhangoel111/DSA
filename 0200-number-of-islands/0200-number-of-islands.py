from collections import deque

class Solution(object):
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]
        islands = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):

                if grid[i][j] == "1" and not visited[i][j]:

                    islands += 1

                    queue = deque()
                    queue.append((i, j))
                    visited[i][j] = True

                    while queue:
                        row, col = queue.popleft()

                        for dr, dc in directions:
                            new_row = row + dr
                            new_col = col + dc

                            if (0 <= new_row < m and
                                0 <= new_col < n and
                                grid[new_row][new_col] == "1" and
                                not visited[new_row][new_col]):

                                visited[new_row][new_col] = True
                                queue.append((new_row, new_col))

        return islands


        