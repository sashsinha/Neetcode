import collections

class Solution:
    def bfs(self, grid: list[list[str]], m: int, n: int, r: int, c: int,
            visited: set[tuple[int, ...]]) -> None:
        queue = collections.deque([(r, c)])
        visited.add((r, c))
        while queue:
            curr_r, curr_c = queue.pop()
            for dy, dx in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                new_r, new_c = curr_r + dy, curr_c + dx
                new_cords = (new_r, new_c)
                if 0 <= new_r < m and 0 <= new_c < n \
                        and grid[new_r][new_c] == '1' \
                        and new_cords not in visited:
                    visited.add(new_cords)
                    queue.appendleft(new_cords)

    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        num_islands = 0
        visited = set()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1' and (row, col) not in visited:
                    num_islands += 1
                    self.bfs(grid, m, n, row, col, visited)
        return num_islands
