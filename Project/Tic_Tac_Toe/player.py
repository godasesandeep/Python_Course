import math
import random


class Player:
    #letter is x or o 
    def __init__(self,letter):
        self.letter=letter

    #we want all players to get their next move given a game
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, game):
        #get random value spot for our next move
        square = random.choice(game.available_moves())
        return square

  
class HumanPlayer(Player): #need not to inharite the class
    def __init__(self,letter):
        super().__init__(letter) #not required to inharite 

    def get_move(self, game):
        valid_square=False
        val=None
        while not valid_square:
            square=input(self.letter +'\'s turn . Input moves (0-8) : ')
            #we are going to check that this is a correct value by trying to cast
            #It is an intiger , if not then we say invalid 
            #if spot is not available on the board then we say it's invalid
            try:
                val=int(square) # if user not enter the intiger then this type cast raise an error
                if val not in game.available_moves(): #check move available or valid number
                    raise ValueError
                valid_square=True
            except ValueError:
                print('Invalid square . try again...')

        return val

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself 'o'
        other_player = 'o' if player == 'x' else 'x'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        #Initializing
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best


class SmartPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        if len(game.available_moves())==9:
            square=random.choice(game.available_moves())
            return square
        else:
            square=self.minimax(game,self.letter)['position']
            return square
        
    def minimax(self,game,player):
        max_player=self.letter
        other_player= 'o' if player=='x' else 'x'

        #base condition /exit condition/previous move check
        if game.current_winner==other_player:
            return {'position':None,'score': 1*(game.num_empty_squares()+1) if other_player==max_player else -1*(game.num_empty_squares()+1)}
        if not game.empty_squares():
            return {"position":None,'score':0}
        #initializing
        if player==max_player:
            best={"position":None,'score':-math.inf}
        else:
            best={"position":None,'score':math.inf}
        

        #simulate by making move
        for position in game.available_moves():
            game.make_move(position,player)
            sim_score=self.minimax(game,other_player)
        
            #undo the move
            game.board[position]=' '
            game.current_winner=None
            sim_score['position']=position

            #assign best score for both
            if player==max_player:
                if sim_score['score']> best['score']:
                    best=sim_score
            else:
                if sim_score['score']<best['score']:
                    best=sim_score

        return best
