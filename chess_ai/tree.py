from chess import Board, Move
from typing import Optional, List


class NodeData:

    def __init__(self, board: Board, move: Optional[Move], score: Optional[int]):
        self.board = board
        self.move = move
        self.score = score


class Node:
    
    def __init__(self, data: NodeData, parent: Optional['Node'] = None):
        self.parent = parent
        self.nodes: List['Node'] = []
        self.data = data
    
    def add_child(self, node: 'Node'):
        self.nodes.append(node)

    def children(self) -> List['Node']:
        return self.nodes

    def is_leaf(self) -> bool:
        return len(self.nodes) == 0
    

class Tree:

    def __init__(self, root):
        self.root: Node = root