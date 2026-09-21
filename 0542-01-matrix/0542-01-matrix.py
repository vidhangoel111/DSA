from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])
        distance = [[-1]*n for _ in range(m)]
        queue = deque()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    distance[i][j] = 0
        while queue:
            row,col = queue.popleft()

            for dr,dc in directions:
                new_row = row + dr
                new_col = col + dc

                if(0 <= new_row < m and 0 <= new_col < n and distance[new_row][new_col]== -1):
                    distance[new_row][new_col] = distance[row][col] + 1
                    queue.append((new_row,new_col))
        return distance


        

        