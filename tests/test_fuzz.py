from woke.testing import *
from woke.testing.fuzzing import *
from pytypes.contracts.sudokuchecker import SudukoChecker
from random import shuffle, randint

class SudukuCheckerTest(FuzzTest):
    checker: SudukoChecker
    board = [[0 for j in range(9)] for i in range(9)]

    def pre_sequence(self) -> None:
        self.checker = SudukoChecker.deploy()
    
    def pre_flow(self, flow_check) -> None:
        generator = SudukoBoardGenerator()
        generator.fillGrid()
        self.board = generator.getBoard()
        print(self.board)
    
    @flow()
    def flow_check(self) -> None:   
        isValid = self.checker.check(self.board)
        assert isValid
        # test invalid board by swaping element in valid board
        row_pos, col_pos = randint(0, 8), randint(0, 8)
        next_row_pos, next_col_pos = randint(0, 8), randint(0, 8)
        if self.board[row_pos][col_pos] != self.board[next_row_pos][next_col_pos]:
            self.board[row_pos][col_pos], self.board[next_row_pos][next_col_pos] = self.board[next_row_pos][next_col_pos], self.board[row_pos][col_pos]
            isInvalid = self.checker.check(self.board)
            assert not isInvalid

@default_chain.connect()
def test_Check():
    default_chain.set_default_accounts(default_chain.accounts[0])
    SudukuCheckerTest().run(sequences_count=30, flows_count=50)

class SudukoBoardGenerator:
    grid = []
    numberList=[1,2,3,4,5,6,7,8,9]

    def __init__(self):
        self.counter = 0
        self.grid = []
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])  

    def getBoard(self):
        return self.grid

    def checkGrid(self):
        for row in range(0,9):
            for col in range(0,9):
                if self.grid[row][col]==0:
                    return False

        return True 

    def fillGrid(self):
        for i in range(0,81):
            row=i//9
            col=i%9
            if self.grid[row][col]==0:
                shuffle(self.numberList)      
                for value in self.numberList:
                    if not(value in self.grid[row]):
                        if not value in (self.grid[0][col],self.grid[1][col],self.grid[2][col],self.grid[3][col],self.grid[4][col],self.grid[5][col],self.grid[6][col],self.grid[7][col],self.grid[8][col]):
                            square=[]
                            if row<3:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(0,3)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(0,3)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(0,3)]
                            elif row<6:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(3,6)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(3,6)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(3,6)]
                            else:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(6,9)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(6,9)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(6,9)]
                            #Check that this value has not already be used on this 3x3 square
                            if not value in (square[0] + square[1] + square[2]):
                                self.grid[row][col]=value
                                if self.checkGrid():
                                    return True
                                else:
                                    if self.fillGrid():
                                        return True
                break
        self.grid[row][col]=0    

    def solveGrid(self):
        #Find next empty cell
        for i in range(0,81):
            row=i//9
            col=i%9
            if self.grid[row][col]==0:
                for value in range (1,10):
                    if not(value in self.grid[row]):
                        if not value in (self.grid[0][col],self.grid[1][col],self.grid[2][col],self.grid[3][col],self.grid[4][col],self.grid[5][col],self.grid[6][col],self.grid[7][col],self.grid[8][col]):
                            square=[]
                            if row<3:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(0,3)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(0,3)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(0,3)]
                            elif row<6:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(3,6)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(3,6)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(3,6)]
                            else:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(6,9)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(6,9)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(6,9)]
                            if not value in (square[0] + square[1] + square[2]):
                                self.grid[row][col]=value
                                if self.checkGrid():
                                    counter+=1
                                    break
                                else:
                                    if self.solveGrid():
                                        return True
                break
        self.grid[row][col]=0  
