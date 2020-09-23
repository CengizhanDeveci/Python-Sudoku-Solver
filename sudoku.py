
class Sudoku():
    def __init__(self):
        self.board= [
            [8,0,0,0,0,0,0,0,0],
            [0,0,3,6,0,0,0,0,0],
            [0,7,0,0,9,1,2,0,0],
            [0,5,0,0,0,7,0,0,0],
            [0,0,0,0,4,5,7,0,0],
            [0,0,0,1,0,0,0,3,0],
            [0,0,1,0,0,0,0,6,8],
            [0,0,8,5,0,0,0,1,0],
            [0,9,0,0,0,0,4,0,0]
        ]

        self.printBoard()
        self.solve()
        print("Result:")
        self.printBoard()

    def solve(self):
        po = self.find_empty()
        if not po:
            return True

        for i in range(1,10):
            if self.valid(i,po):
                self.board[po[0]][po[1]] = i
                if self.solve():
                    return True


                self.board[po[0]][po[1]] = 0
        return False    


    def valid(self,num,pos):        
        for i in range(len(self.board)):
            if self.board[pos[0]][i] == num and i != pos[1]:
                return False
        for j in range(len(self.board)):
            if self.board[j][pos[1]] == num and j != pos[0]:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.board[i][j] == num and (i,j) != pos:
                    return False

        return True

    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i,j)
        return None

    def printBoard(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("----------------------------")
            for j in range(len(self.board)):
                if j % 3 == 0 and j != 0:
                    print(" | ",end=" ")
                    print(self.board[i][j],end=" ")
                elif j == 8:
                    print(self.board[i][j])
                else:
                    print(self.board[i][j],end=" ")



if __name__ == "__main__":
    sudoku = Sudoku()
