class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        def CheckRow(rowNum):
            rowSet={"."}
            for i in range(0,9):
                if board[rowNum][i]!=".":
                    if  board[rowNum][i] not in rowSet:
                        rowSet.add(board[rowNum][i])
                        #print(rowSet)
                    else:
                        print("hi row")
                        return False
                
        def CheckColumn(colNum):
            colSet={"."}
            for i in range(0,9):
                if board[i][colNum]!=".":
                    if board[i][colNum] not in colSet:
                        colSet.add(board[i][colNum])
                    else:
                        print("hi col")
                        return False
        
        def CheckSubBox(rowNum,colNum):
            subBoxSet={"."}
            for i in range(rowNum,rowNum+3):
                for j in range(colNum,colNum+3):
                    if board[i][j]!=".":
                        if board[i][j] not in subBoxSet:
                            subBoxSet.add(board[i][j])
                        else:
                            return False
        
        #first check all the rows
        for i in range(0,9):
            if CheckRow(i) == False:
                return False
            
        #next check all columns
        for i in range(0,9):
            if CheckColumn(i) == False:
                return False
        
        #now check SubBoxes
        for m in [0,3,6]:
            for n in [0,3,6]:
                if CheckSubBox(m,n) == False:
                    return False
                
        return True
