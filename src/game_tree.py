"""
Game tree examples for the Minimax and Alpha-Beta laboratory.

A tree is represented using nested lists.
- Internal nodes are lists.
- Leaf nodes are integer scores.

The maximizing player tries to obtain the highest value.
The minimizing player tries to obtain the lowest value.
"""

from typing import TypeAlias

GameTree: TypeAlias = int | list["GameTree"]


def sample_tree() -> GameTree:
    """
    Returns a small tree for classroom demonstration.

    Expected result: 5
    """
    return [
        [3, 5],
        [2, 9],
    ]


def medium_tree() -> GameTree:
    """
    Returns a medium-sized tree where Alpha-Beta can prune branches.

    Expected result: 6
    """
    return [
        [[3, 5], [6, 9]],
        [[1, 2], [0, -1]],
        [[7, 4], [8, 6]],
    ]


def ordered_tree_for_pruning() -> GameTree:
    """
    Tree intentionally ordered to help Alpha-Beta prune more effectively.

    Expected result: 10
    """
    return [
        [[10, 9], [8, 7]],
        [[6, 5], [4, 3]],
        [[2, 1], [0, -1]],
    ]