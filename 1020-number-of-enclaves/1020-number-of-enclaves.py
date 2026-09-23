class Solution(object):
    def numEnclaves(self, grid):
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            visited[row][col] = True

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (0 <= new_row < m and
                    0 <= new_col < n and
                    grid[new_row][new_col] == 1 and
                    not visited[new_row][new_col]):

                    dfs(new_row, new_col)

        # Start DFS from all boundary land cells
        for i in range(m):
            for j in range(n):
                if ((i == 0 or i == m - 1 or j == 0 or j == n - 1)
                        and grid[i][j] == 1
                        and not visited[i][j]):

                    dfs(i, j)

        # Remaining unvisited land cells are enclaves
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1

        return count