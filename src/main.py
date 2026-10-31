"""
Main execution file for the Alpha-Beta laboratory.
"""

from src.alpha_beta import alpha_beta
from src.game_tree import medium_tree, ordered_tree_for_pruning, sample_tree
from src.minimax import minimax


def compare_algorithms(tree_name: str, tree) -> None:
    """Prints a comparison between Minimax and Alpha-Beta."""
    minimax_result = minimax(tree)
    alpha_beta_result = alpha_beta(tree)

    print(f"\nTree: {tree_name}")
    print("-" * 40)
    print(f"Minimax value: {minimax_result.value}")
    print(f"Minimax nodes evaluated: {minimax_result.nodes_evaluated}")
    print(f"Alpha-Beta value: {alpha_beta_result.value}")
    print(f"Alpha-Beta nodes evaluated: {alpha_beta_result.nodes_evaluated}")
    print(f"Alpha-Beta branches pruned: {alpha_beta_result.branches_pruned}")


def main() -> None:
    """Runs the laboratory examples."""
    compare_algorithms("Sample Tree", sample_tree())
    compare_algorithms("Medium Tree", medium_tree())
    compare_algorithms("Ordered Tree", ordered_tree_for_pruning())


if __name__ == "__main__":
    main()