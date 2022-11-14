from chess import Board
from .chess_player import Player
from .board_state import game_complete
from chess import svg


class Game:
    def __init__(self):
        self.board = Board()
        self.draw_counter = 0

    # Return svgs for a game so it can be renders in jupyter notebook
    def render_game(self, player_1: Player, player_2: Player):
        current_player = None
        players = [player_1, player_2]
        svgs = []
        print('game starts')
        while (result := game_complete(self.board)) == None:
            current_player = players.pop(0)
            players.append(current_player)
            current_player.move(self.board)

            svgs.append(svg.board(self.board, size=300))

        return svgs


    # Plays chess and returns winning player, or None for a draw
    def play(self, player_1: Player, player_2: Player) -> Player:
        current_player = None
        players = [player_1, player_2]
        while (result := game_complete(self.board)) == None:
            current_player = players.pop(0)
            players.append(current_player)
            current_player.move(self.board)


        if result == 'white':
            return player_1
        if result == 'black':
            return player_2
        if result == 'draw':
            return None
        raise Exception('something when wrong')

    
    def play_and_get_turns_played(self, player_1: Player, player_2: Player):
        current_player = None
        players = [player_1, player_2]
        turns = 0
        while (result := game_complete(self.board)) == None:
            current_player = players.pop(0)
            players.append(current_player)
            current_player.move(self.board)
            turns += 1


        if result == 'white':
            return (player_1, turns)
        if result == 'black':
            return (player_2, turns)
        if result == 'draw':
            return (None, turns)
        raise Exception('something when wrong')