from chess import Board
from typing import Optional

color = {
    True: 'white',
    False: 'black'
    }

# None, or draw/white/black
def game_complete(board: Board) -> Optional[str]:
    last_move = color[not board.turn]
    if board.is_checkmate() or board.is_variant_loss():
        if last_move == 'white':
            return 'white'
        else:
            return 'black'

    if is_draw_state(board):
        return 'draw'
    return None


def is_draw_state(board: Board) -> bool:
    return board.can_claim_fifty_moves() or board.is_stalemate()
