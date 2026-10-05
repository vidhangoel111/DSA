import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        # Minimum effort required to reach each cell
        effort = [[float('inf')] * cols for _ in range(rows)]

        # Starting cell requires 0 effort
        effort[0][0] = 0

        # Min heap: (effort, row, column)
        heap = []
        heapq.heappush(heap, (0, 0, 0))

        # Up, Down, Left, Right
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while heap:
            current_effort, row, col = heapq.heappop(heap)

            # We reached the destination
            if row == rows - 1 and col == cols - 1:
                return current_effort

            # Explore 4 neighbours
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                # Check if neighbour is inside the grid
                if 0 <= new_row < rows and 0 <= new_col < cols:

                    # Difference between current and neighbouring cell
                    height_difference = abs(
                        heights[row][col] - heights[new_row][new_col]
                    )

                    # Effort of the new path
                    new_effort = max(
                        current_effort,
                        height_difference
                    )

                    # If this is a better path to the neighbour
                    if new_effort < effort[new_row][new_col]:
                        effort[new_row][new_col] = new_effort

                        heapq.heappush(
                            heap,
                            (new_effort, new_row, new_col)
                        )

        return 0