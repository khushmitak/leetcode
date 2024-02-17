"""METHOD: To check if the sudoku is valid, check if the element at the current row, column index does not already
exist in that particular row, column and 3 * 3 square, if it does -- the sudoku is not valid, return false.
If the element is not present in the set already, then add that element to row, column and square to keep the sudoku updated.

"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in boxes[(r // 3, c // 3)]
                    ):
                    return False
            
                cols[c].add(board[r][c])
                rows[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        
        return True