from ..chess_game import Game
from ..chess_player import RandomAgent


def test_if_game_ends_with_random_play():
    game = Game()
    player_1 = RandomAgent('Jane')
    player_2 = RandomAgent('Billy')
    
    result = game.play(player_1, player_2)

    assert result == None or result == player_1 or result == player_2


def test_if_game_ends_with_random_play_without_draw():
    game = Game()
    player_1 = RandomAgent('Jane')
    player_2 = RandomAgent('Billy')
    
    result = game.play(player_1, player_2)
    while result == None:
        game = Game()
        result = game.play(player_1, player_2)

    assert result == None or result == player_1 or result == player_2


def test_10_games_for_errors():
    for i in range(10):
        test_if_game_ends_with_random_play()


def test_10_games_for_errors_without_draw():
    for i in range(10):
        test_if_game_ends_with_random_play_without_draw()


def test_win_condition():
    game = Game()
    player_1 = RandomAgent('Jane')
    player_2 = RandomAgent('Billy')

    color = {
        'white': True,
        'black': False
    }

    result = game.play(player_1, player_2)

    while result == None: # is a Draw
        game = Game()
        result = game.play(player_1, player_2)
        print(result)

    if result.name == 'Jane':
        # if p1 is white.
        # if p1 wins, python-chess will show that it is p2s turn, because p1 just moved. 
        # I return the player who last moved.
        assert game.board.turn == color['black']
    else:
        assert game.board.turn == color['white']


def test_win_condition_black():
    game = Game()
    player_1 = RandomAgent('Jane')
    player_2 = RandomAgent('Billy')

    color = {
        'white': True,
        'black': False
    }

    result = game.play(player_1, player_2)

    while result == None or result.name == 'Jane': # is a Draw
        game = Game()
        result = game.play(player_1, player_2)
        print(result)

    assert game.board.turn == color['white']
    

def test_win_condition_white():
    game = Game()
    player_1 = RandomAgent('Jane')
    player_2 = RandomAgent('Billy')

    color = {
        'white': True,
        'black': False
    }

    result = game.play(player_1, player_2)

    while result == None or result.name == 'Billy': # is a Draw
        game = Game()
        result = game.play(player_1, player_2)
        print(result)

    assert game.board.turn == color['black']
