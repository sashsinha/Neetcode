import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = 9
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sub_boxes = collections.defaultdict(set)
        for r in range(n):
            for c in range(n):
                val = board[r][c]
                if val == '.':
                    continue
                if val in rows[r]:
                    return False
                rows[r].add(val)
                if val in cols[c]:
                    return False
                cols[c].add(val)
                sub_box_coords = (r // 3, c // 3)
                if val in sub_boxes[sub_box_coords]:
                    return False
                sub_boxes[sub_box_coords].add(val)
        return True
