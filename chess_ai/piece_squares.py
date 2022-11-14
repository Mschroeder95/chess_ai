from chess import Board, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING, WHITE, square_name


PAWNS_TABLE = {
    'a1': 0,'a2': 5,'a3': 5,'a4': 0,'a5': 5,'a6': 10,'a7': 50,'a8': 0,
    'b1': 0,'b2': 10,'b3': -5,'b4': 0,'b5': 5,'b6': 10,'b7': 50,'b8': 0,
    'c1': 0,'c2': 10,'c3': -10,'c4': 0,'c5': 10,'c6': 20,'c7': 50,'c8': 0,
    'd1': 0,'d2': -20,'d3': 0,'d4': 20,'d5': 25,'d6': 30,'d7': 50,'d8': 0,
    'e1': 0,'e2': -20,'e3': 0,'e4': 20,'e5': 25,'e6': 30,'e7': 50,'e8': 0,
    'f1': 0,'f2': 10,'f3': -10,'f4': 0,'f5': 10,'f6': 20,'f7': 50,'f8': 0,
    'g1': 0,'g2': 10,'g3': -5,'g4': 0,'g5': 5,'g6': 10,'g7': 50,'g8': 0,
    'h1': 0,'h2': 5,'h3': 5,'h4': 0,'h5': 5,'h6': 10,'h7': 50,'h8': 0,
}

KNIGHTS_TABLE = {
    'a1': -50,'a2': -40,'a3': -30,'a4': -30,'a5': -30,'a6': -30,'a7': -40,'a8': -50,
    'b1': -40,'b2': -20,'b3': 5,'b4': 0,'b5': 5,'b6': 0,'b7': -20,'b8': -40,
    'c1': -30,'c2': 0,'c3': 10,'c4': 15,'c5': 15,'c6': 10,'c7': 0,'c8': -30,
    'd1': -30,'d2': 5,'d3': 15,'d4': 20,'d5': 20,'d6': 15,'d7': 0,'d8': -30,
    'e1': -30,'e2': 5,'e3': 15,'e4': 20,'e5': 20,'e6': 15,'e7': 0,'e8': -30,
    'f1': -30,'f2': 0,'f3': 10,'f4': 15,'f5': 15,'f6': 10,'f7': 0,'f8': -30,
    'g1': -40,'g2': -20,'g3': 5,'g4': 0,'g5': 5,'g6': 0,'g7': -20,'g8': -40,
    'h1': -50,'h2': -40,'h3': -30,'h4': -30,'h5': -30,'h6': -30,'h7': -40,'h8': -50,
}

BISHOPS_TABLE = {
    'a1': -20,'a2': -10,'a3': -10,'a4': -10,'a5': -10,'a6': -10,'a7': -10,'a8': -20,
    'b1': -10,'b2': 5,'b3': 10,'b4': 0,'b5': 5,'b6': 0,'b7': 0,'b8': -10,
    'c1': -10,'c2': 0,'c3': 10,'c4': 10,'c5': 5,'c6': 5,'c7': 0,'c8': -10,
    'd1': -10,'d2': 0,'d3': 10,'d4': 10,'d5': 10,'d6': 10,'d7': 0,'d8': -10,
    'e1': -10,'e2': 0,'e3': 10,'e4': 10,'e5': 10,'e6': 10,'e7': 0,'e8': -10,
    'f1': -10,'f2': 0,'f3': 10,'f4': 10,'f5': 5,'f6': 5,'f7': 0,'f8': -10,
    'g1': -10,'g2': 5,'g3': 10,'g4': 0,'g5': 5,'g6': 0,'g7': 0,'g8': -10,
    'h1': -20,'h2': -10,'h3': -10,'h4': -10,'h5': -10,'h6': -10,'h7': -10,'h8': -20,
}

ROOKS_TABLE = {
    'a1': 0,'a2': -5,'a3': -5,'a4': -5,'a5': -5,'a6': -5,'a7': 5,'a8': 0,
    'b1': 0,'b2': 0,'b3': 0,'b4': 0,'b5': 0,'b6': 0,'b7': 10,'b8': 0,
    'c1': 0,'c2': 0,'c3': 0,'c4': 0,'c5': 0,'c6': 0,'c7': 10,'c8': 0,
    'd1': 5,'d2': 0,'d3': 0,'d4': 0,'d5': 0,'d6': 0,'d7': 10,'d8': 0,
    'e1': 5,'e2': 0,'e3': 0,'e4': 0,'e5': 0,'e6': 0,'e7': 10,'e8': 0,
    'f1': 0,'f2': 0,'f3': 0,'f4': 0,'f5': 0,'f6': 0,'f7': 10,'f8': 0,
    'g1': 0,'g2': 0,'g3': 0,'g4': 0,'g5': 0,'g6': 0,'g7': 10,'g8': 0,
    'h1': 0,'h2': -5,'h3': -5,'h4': -5,'h5': -5,'h6': -5,'h7': 5,'h8': 0,
}

QUEEN_TABLE = {
    'a1': -20,'a2': -10,'a3': -10,'a4': 0,'a5': -5,'a6': -10,'a7': -10,'a8': -20,
    'b1': -10,'b2': 0,'b3': 5,'b4': 0,'b5': 0,'b6': 0,'b7': 0,'b8': -10,
    'c1': -10,'c2': 5,'c3': 5,'c4': 5,'c5': 5,'c6': 5,'c7': 0,'c8': -10,
    'd1': -5,'d2': 0,'d3': 5,'d4': 5,'d5': 5,'d6': 5,'d7': 0,'d8': -5,
    'e1': -5,'e2': 0,'e3': 5,'e4': 5,'e5': 5,'e6': 5,'e7': 0,'e8': -5,
    'f1': -10,'f2': 0,'f3': 5,'f4': 5,'f5': 5,'f6': 5,'f7': 0,'f8': -10,
    'g1': -10,'g2': 0,'g3': 0,'g4': 0,'g5': 0,'g6': 0,'g7': 0,'g8': -10,
    'h1': -20,'h2': -10,'h3': -10,'h4': -0,'h5': -5,'h6': -10,'h7': -10,'h8': -20,
}

# TODO: ADD use endgame King piece table also
KING_TABLE = {
    'a1': 20,'a2': 20,'a3': -10,'a4': -20,'a5': -30,'a6': -30,'a7': -30,'a8': -30,
    'b1': 30,'b2': 20,'b3': -20,'b4': -30,'b5': -40,'b6': -40,'b7': -40,'b8': -40,
    'c1': 10,'c2': 0,'c3': -20,'c4': -30,'c5': -40,'c6': -40,'c7': -40,'c8': -40,
    'd1': 0,'d2': 0,'d3': -20,'d4': -40,'d5': -50,'d6': -50,'d7': -50,'d8': -50,
    'e1': 0,'e2': 0,'e3': -20,'e4': -40,'e5': -50,'e6': -50,'e7': -50,'e8': -50,
    'f1': 10,'f2': 0,'f3': -20,'f4': -30,'f5': -40,'f6': -40,'f7': -40,'f8': -40,
    'g1': 30,'g2': 20,'g3': -20,'g4': -30,'g5': -40,'g6': -40,'g7': -40,'g8': -40,
    'h1': 20,'h2': 20,'h3': -10,'h4': -20,'h5': -30,'h6': -30,'h7': -30,'h8': -30,
}


def score_white_pawns(board: Board) -> int:
    pieces = board.pieces(piece_type=PAWN, color=WHITE)
    score = 0
    for p in pieces:
        score += PAWNS_TABLE[square_name(p)]

    return score


def score_white_knights(board: Board) -> int:
    pieces = board.pieces(piece_type=KNIGHT, color=WHITE)
    score = 0
    for p in pieces:
        score += KNIGHTS_TABLE[square_name(p)]

    return score


def score_white_bishops(board: Board) -> int:
    pieces = board.pieces(piece_type=BISHOP, color=WHITE)
    score = 0
    for p in pieces:
        score += BISHOPS_TABLE[square_name(p)]

    return score


def score_white_rooks(board: Board) -> int:
    pieces = board.pieces(piece_type=ROOK, color=WHITE)
    score = 0
    for p in pieces:
        score += ROOKS_TABLE[square_name(p)]

    return score
    

def score_white_queen(board: Board) -> int:
    pieces = board.pieces(piece_type=QUEEN, color=WHITE)
    score = 0
    for p in pieces:
        score += QUEEN_TABLE[square_name(p)]

    return score


def score_white_king(board: Board) -> int:
    pieces = board.pieces(piece_type=KING, color=WHITE)
    score = 0
    for p in pieces:
        score += KING_TABLE[square_name(p)]

    return score


def get_board_score_white(board: Board) -> int:
    score = 0
    score += score_white_pawns(board)
    score += score_white_bishops(board)
    score += score_white_knights(board)
    score += score_white_queen(board)
    score += score_white_rooks(board)
    score += score_white_king(board)

    return score
