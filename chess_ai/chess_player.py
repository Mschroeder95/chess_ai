from chess import Board, Move
from abc import abstractmethod
import random
from .tree import Tree, Node, NodeData
from typing import List
from .piece_squares import get_board_score_white
from .board_state import game_complete


class Player:

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def move(self) -> bool:
        pass


class RandomAgent(Player):

    def move(self, board: Board) -> bool:
        if board.legal_moves.count() == 0:
            # can't move means they lose in board.is_variant_win
            return False

        legal_moves = []
        for move in board.legal_moves:
            legal_moves.append(move)
        
        move = legal_moves[random.randint(0,len(legal_moves)-1)]
        board.push(move)
                
        return True


# Very slow at depth 3
class PieceSquaresAgent(Player):

    tree: Tree

    def __init__(self, name: str, depth: int):
        self.name = name
        self.depth = depth - 1 # because I prime the first layer

    def move(self, board: Board) -> bool:
        if board.legal_moves.count() == 0:
            # can't move means they lose in board.is_variant_win
            return False

        data = NodeData(board, None, None)
        root = Node(data)

        for m in board.legal_moves:
            new_board = board.copy(stack=False)
            new_board.push(m)
            score = get_board_score_white(new_board)
            node_data = NodeData(new_board, m, score)
            root.add_child(Node(node_data))

        self.tree = Tree(root)

        node_layer = root.children()
        scoring_stack: List[Node] = []
        for i in range(self.depth):
            next_layer: List[Node] = []
            for node in node_layer:
                if node.is_leaf():
                    for m in node.data.board.legal_moves:
                        new_board = node.data.board.copy(stack=False)
                        new_board.push(m)
                        score = get_board_score_white(new_board)
                        node_data = NodeData(new_board, m, score)
                        new_node = Node(node_data, parent=node)
                        node.add_child(new_node)
                        next_layer.append(new_node)
                        scoring_stack.append(new_node)
            node_layer = next_layer

        for i in range(len(scoring_stack)):
            node = scoring_stack.pop()
            node.parent.data.score += node.data.score

        best_node = None
        for node in self.tree.root.children():
            if best_node == None:
                best_node = node
            else:
                if node.data.score > best_node.data.score:
                    best_node = node
        
        move = best_node.data.move

        board.push(move)
        return True
            

class MonteCarloAgent(Player):
    tree: Tree
    WEIGHTS = {
        'persist': 0,
    }

    def __init__(self, name: str, depth: int, path_count: int, win_weight:int=5, draw_weight:int=1, lose_weight:int=-1):
        self.name = name
        self.depth = depth 
        self.path_count = path_count
        self.WEIGHTS['lose'] = lose_weight
        self.WEIGHTS['win'] = win_weight
        self.WEIGHTS['draw'] = draw_weight


    def move(self, board: Board) -> bool:
        if board.legal_moves.count() == 0:
            # can't move means they lose in board.is_variant_win
            return False

        data = NodeData(board, None, 0)
        root = Node(data)
        self.tree = Tree(root)

        scoring_stack: List[Node] = []
                
        current_node = self.tree.root
        # create random paths equal to path_count
        for p in range(self.path_count):
            # each path should be depth deep, unless an end condition in met
            for d in range(self.depth):
                legal_moves = []
                for move in current_node.data.board.legal_moves:
                    legal_moves.append(move)

                move = legal_moves[random.randint(0,len(legal_moves)-1)]
                new_board = current_node.data.board.copy(stack=False)
                new_board.push(move)

                score = 0
                result = game_complete(new_board)
                # check the state of the game after moving
                if result == None:
                    score = self.WEIGHTS['persist']
                elif result == 'white':
                    score = self.WEIGHTS['win']
                elif result == 'black':
                    score = self.WEIGHTS['lose']
                elif result == 'draw':
                    score = self.WEIGHTS['draw']
                    
                # add node with score from above
                data = NodeData(new_board, move, score)
                new_node = Node(data, current_node)
                current_node.add_child(new_node)
                current_node = new_node

                # if end conditon is met, break loop and create another path
                if result is not None:
                    break
    
            scoring_stack.append(current_node) # leaf
            current_node = self.tree.root # go back to root


        # iterate from the leaf nodes up to the root, adding score to parent along the way
        for leaf in scoring_stack:
            current_node = leaf
            while current_node != self.tree.root:
                current_node.parent.data.score = current_node.parent.data.score + current_node.data.score
                current_node = current_node.parent

        best_node = None

        # find the best score in root children since scores were propegated up from the leaves
        for node in self.tree.root.children():
            if best_node == None:
                best_node = node
            else:
                if node.data.score > best_node.data.score:
                    best_node = node
                    
        move = best_node.data.move

        board.push(move)
        return True



# Not used in data_collection
# This is only used in the spectate.ipynb notebook to watch PieceSquares and MonteCarlo play against eachother.
# Could probably be one class with above, but didn't want to mess anything up.
class MonteCarloAgentBlack(Player):
    tree: Tree
    WEIGHTS = {
        'persist': 0,
    }

    def __init__(self, name: str, depth: int, path_count: int, win_weight:int=5, draw_weight:int=1, lose_weight:int=-1):
        self.name = name
        self.depth = depth 
        self.path_count = path_count
        self.WEIGHTS['lose'] = lose_weight
        self.WEIGHTS['win'] = win_weight
        self.WEIGHTS['draw'] = draw_weight


    def move(self, board: Board) -> bool:
        if board.legal_moves.count() == 0:
            # can't move means they lose in board.is_variant_win
            return False

        data = NodeData(board, None, 0)
        root = Node(data)
        self.tree = Tree(root)

        scoring_stack: List[Node] = []
                
        current_node = self.tree.root
        for p in range(self.path_count):
            for d in range(self.depth):
                legal_moves = []
                for move in current_node.data.board.legal_moves:
                    legal_moves.append(move)

                move = legal_moves[random.randint(0,len(legal_moves)-1)]
                new_board = current_node.data.board.copy(stack=False)
                new_board.push(move)

                score = 0
                result = game_complete(new_board)
                if result == None:
                    score = self.WEIGHTS['persist']
                elif result == 'black':
                    score = self.WEIGHTS['win']
                elif result == 'white':
                    score = self.WEIGHTS['lose']
                elif result == 'draw':
                    score = self.WEIGHTS['draw']
                    
                data = NodeData(new_board, move, score)
                new_node = Node(data, current_node)
                current_node.add_child(new_node)
                current_node = new_node
                if result is not None:
                    break
    
            scoring_stack.append(current_node) # leaf
            current_node = self.tree.root # go back to root

        for leaf in scoring_stack:
            current_node = leaf
            while current_node != self.tree.root:
                current_node.parent.data.score = current_node.parent.data.score + current_node.data.score
                current_node = current_node.parent

        best_node = None

        for node in self.tree.root.children():
            if best_node == None:
                best_node = node
            else:
                if node.data.score > best_node.data.score:
                    best_node = node
                    
        move = best_node.data.move
        
        # Try to save some time by keeping the childen under the used move
        self.tree.root = best_node

        board.push(move)
        return True
