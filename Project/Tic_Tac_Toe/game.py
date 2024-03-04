from player import HumanPlayer,RandomComputerPlayer,SmartComputerPlayer,SmartPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board=[' ' for _ in range(9)] #we use single list to represent 3X3 board
        self.current_winner=None #keep track of winner !

    def print_board(self):
        #this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row)+ ' |')

        #print actual board with values | X |   |   | .. ... .. .. 
    @staticmethod
    def print_board_num():
        # 0 | 1| 2 ete (tells us what number corresponds to what box)
        number_board=[[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row)+ ' |')
        # it prints | 0 | 1 | 2 | . .. .. .

    def available_moves(self):
        moves=[] #list of index moves available
        for (i,slot) in enumerate(self.board):
            #[x,x,o]==> [(0,x),(1,x),(2,o)]
            if slot==' ':
                moves.append(i)
        return moves
        #or you can write like this
        #return [i if slot==' ' else '' for (i,slot) in enumerate(self.board)]
        #return [i for i,slot in enumerate(self.board) if spot==' ']
        #it returns [0,1,2,3,4,5,6,7,8]
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return len(self.available_moves())
        #or return self.board.count(' ')
    
    def make_move(self,square,letter):
        #if valid move ,then make the move (assign the square to letter)
        #then return True . if invalid then return False
        if self.board[square]==' ':
            self.board[square]=letter
            if self.winner(square,letter):
                self.current_winner=letter
            return True
        return False
    
    def winner(self,square,letter):
        #winner if 3 row anyware ..we have to check all these !
        #Firs't let check row
        row_ind=square//3
        row=self.board[row_ind*3:(row_ind+1)*3]
        if all([spot==letter for spot in row]):
            return True
        
        #check for column
        col_ind=square%3
        column=[self.board[col_ind+i*3] for i in range(3)]
        if all([spot==letter for spot in column]):
            return True
    
        # check for diagonams ,only if number is even or diagonal num(0,2,4,6,8)
        if square%2==0:
            diagonal1=[self.board[i] for i in [0,4,8]]
            if all([spot==letter for spot in diagonal1]):
                return True
            diagonal2=[self.board[i] for i in [2,4,6]]
            if all([spot==letter for spot in diagonal2]):
                return True
            return False

    
def play(game,x_player,o_player,print_game=True):
    #return the winner of the game(letter) ! or None for a tie
    if print_game:
        game.print_board_num()

    letter = 'x' #starting letter
    #iterate while the games still has empty squares
    #we don't have to worry about winner because we will just return that which brakes the loop
    while game.empty_squares():
        #get the move from appropriate player
        if letter=='o':
            square=o_player.get_move(game) #take input from player o
        else:
            square=x_player.get_move(game) # take input from player x
            
        #let's define function to make a move !
        if game.make_move(square,letter):
            if print_game:
                print(letter+ f' make a move to square {square}')
                game.print_board()
                print('') # just empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' win\'s the game')
                return letter
            # after make a move we need to alter the letter(switching between the letters)
            if letter == 'x':
                letter='o'
            else:
                letter='x'
            #or we can write, letter ='o' if letter=='x' else 'x'
            #when we win the game ==>After making move we need to check for winner
                    
            # to add tiny brek
            time.sleep(1)

    if print_game:
        print('it\'s tie ...! ')


if __name__ == "__main__":
    x_player=HumanPlayer('x')
    #o_player=RandomComputerPlayer('o')
    #o_player=HumanPlayer('o')
    #o_player=SmartComputerPlayer('o')
    o_player=SmartPlayer('o')
    t=TicTacToe()
    play(t,x_player,o_player,print_game=True)

