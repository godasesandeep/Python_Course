import random
import re

class Board:
    def __init__(self,dim_size,num_bomb):
        self.dim_size=dim_size
        self.num_bomb=num_bomb
        self.board=self.make_board()
        self.assign_value()
        self.dug=set()

    def make_board(self):
        board=[[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        #plant bomb
        bomb=0
        while bomb<self.num_bomb:
            value=random.randint(0,self.dim_size**2-1)
            row=value//self.dim_size
            col=value%self.dim_size
            if board[row][col]=='*':
                continue
            board[row][col]='*'
            bomb +=1
        return board


    def assign_value(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c]=="*":
                    continue
                self.board[r][c]=self.get_num_neighboring_bombs(r,c)

    def get_num_neighboring_bombs(self,row,col):
        num_neighboring_bombs = 0
        for r in range(max(0,row-1),min(self.dim_size-1,row+1)+1):
            for c in range(max(0,col-1),min(self.dim_size-1,col+1)+1):
                if r == row and c == col: #our location need not to check, I think this code need not to write
                    continue
                if self.board[r][c]=="*":
                    num_neighboring_bombs +=1
        return num_neighboring_bombs
    
    def dig(self,row,col):
        self.dug.add((row,col))
        if self.board[row][col]=='*':
            return False
        if self.board[row][col]>0:
            return True
        for r in range(max(0,row-1),min(self.dim_size-1,row+1)+1):
            for c in range(max(0,col-1),min(self.dim_size-1,col+1)+1):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)

        return True
    
    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
    

#play game
    
def play():
    board=Board(10,10)
    safe=True
    while len(board.dug) < board.dim_size**2- board.num_bomb:
        print(board)
        try:
            user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
            row, col = int(user_input[0]), int(user_input[-1])
        except:
            print("Invalid input")
            continue
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid location. Try again.")
            continue
        if (row,col) in board.dug:
            print("already dug ..enter valid location")

        safe=board.dig(row,col)
        if not safe:
            break
    if safe:
        print("Congrates....VICTORY")
    else:
        print("SORRY GAME OVER :(")
        # let's reveal the whole board!
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == "__main__":
    play()


        



