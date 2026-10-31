"""
Minimax implementation.

Minimax explores all possible branches of the tree.
This makes it correct, but expensive when the tree grows.
"""

from dataclasses import dataclass
from src.game_tree import GameTree


@dataclass
class SearchResult:
    """Stores the value found and the number of evaluated leaf nodes."""

    value: int
    nodes_evaluated: int


def is_leaf(node: GameTree) -> bool:
    """Returns True when the node is a terminal score."""
    return isinstance(node, int)


def minimax(node: GameTree, maximizing_player: bool = True) -> SearchResult:
    """
    Executes the Minimax algorithm over a game tree.

    Args:
        node: Tree node represented by nested lists or an integer leaf.
        maximizing_player: True when the current player maximizes.

    Returns:
        SearchResult with the best value and evaluated leaves.
    """
    if is_leaf(node):
        return SearchResult(value=node, nodes_evaluated=1)

    children = node
    results = [minimax(child, not maximizing_player) for child in children]
    total_nodes = sum(result.nodes_evaluated for result in results)

    if maximizing_player:
        best_value = max(result.value for result in results)
    else:
        best_value = min(result.value for result in results)

    return SearchResult(value=best_value, nodes_evaluated=total_nodes)