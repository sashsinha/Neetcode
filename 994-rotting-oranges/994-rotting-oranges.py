import collections
import dataclasses

@dataclasses.dataclass
class CellWithDist:
    row: int
    col: int
    dist: int
        
    def __iter__(self):
        return iter(dataclasses.astuple(self))


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_dist = -1
        saw_fresh = False
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if not saw_fresh:
                        saw_fresh = True
                    dist = self.bfs(grid, m, n, r, c)
                    if dist == -1:
                        return -1
                    max_dist = max(max_dist, dist)
        return max_dist if saw_fresh else 0
        
    def bfs(self, grid: list[list[int]], m: int, n: int, r: int, c: int) -> int:
        queue = collections.deque([CellWithDist(r, c, 0)])
        visited = {(r, c)}
        while queue:
            row, col, dist = queue.pop()
            for dy, dx in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                new_row, new_col = row + dy, col + dx
                if 0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) not in visited:
                    if grid[new_row][new_col] == 2:
                        return dist + 1
                    elif grid[new_row][new_col] == 1:
                        queue.appendleft(CellWithDist(new_row, new_col, dist + 1))
                        visited.add((new_row, new_col))
        return -1