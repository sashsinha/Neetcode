import collections

class Solution:
    def check_valid_nine_cells(self, nine_cells: list[str]) -> bool:
        counts = collections.Counter(nine_cells)
        for k, v in counts.items():
            if v > 1 and k != '.':
                return False
        return True
    
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        sub_boxes = defaultdict(list)
        cols = defaultdict(list)

        for row_idx, row in enumerate(board):
            if not self.check_valid_nine_cells(row):
                return False
            for col_idx, val in enumerate(row):
                cols[col_idx].append(val)
                sub_boxes[(row_idx // 3, col_idx // 3)].append(val)
  
        for col in cols.values():
            if not self.check_valid_nine_cells(col):
                return False
 
        for sub_box in sub_boxes.values():
            if not self.check_valid_nine_cells(sub_box):
                return False

        return True
