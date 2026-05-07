class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        cells = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val in rows[i]:
                    return False

                if val in cols[j]:
                    return False

                if val in cells[(math.floor(i/3),math.floor(j/3))]:
                    return False

                if val != '.':
                    rows[i].add(val)
                    cols[j].add(val)
                    cells[math.floor(i/3),math.floor(j/3)].add(val)     
        
        return True  