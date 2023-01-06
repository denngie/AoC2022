"""Day 8: Treetop Tree House."""
from aocd.models import Puzzle


class Forest:
    """Forest full of trees."""

    def __init__(self, trees: str) -> None:
        """Initiate class."""
        self.trees = trees.splitlines()

    def visible_trees(self) -> int:
        """Count all trees that are visible from the outside."""
        visible_trees = 0

        for v_index, h_tree_line in enumerate(self.trees[1:-1], 1):
            for h_index, tree in enumerate(h_tree_line[1:-1], 1):
                if tree > max(h_tree_line[:h_index]):
                    continue
                if tree > max(h_tree_line[h_index + 1:]):
                    continue

                v_tree_line = [x[h_index] for x in self.trees]
                if tree > max(v_tree_line[:v_index]):
                    continue
                if tree > max(v_tree_line[v_index + 1:]):
                    continue

                visible_trees += 1

        return pow(len(self.trees), 2) - visible_trees

    def _calculate_score(self, tree: str, tree_line: str | reversed | list[str]) -> int:
        """Count all visible trees from a specific tree in a specific direction."""
        score = 0
        for tree_count, adj_tree in enumerate(tree_line, 1):
            score = tree_count
            if adj_tree >= tree:
                return score
        return score

    def max_scenic_score(self) -> int:
        """Count the highest scenir score for all trees."""
        best_scenic_score = 0

        for v_index, h_tree_line in enumerate(self.trees[1:-1], 1):
            for h_index, tree in enumerate(h_tree_line[1:-1], 1):
                v_tree_line = [x[h_index] for x in self.trees]

                # Calculate left, right, up, down
                scenic_score = self._calculate_score(tree, reversed(h_tree_line[:h_index]))
                scenic_score *= self._calculate_score(tree, h_tree_line[h_index + 1:])
                scenic_score *= self._calculate_score(tree, reversed(v_tree_line[:v_index]))
                scenic_score *= self._calculate_score(tree, v_tree_line[v_index + 1:])
                best_scenic_score = max(best_scenic_score, scenic_score)

        return best_scenic_score


def main() -> None:
    """Solve the puzzle."""
    puzzle = Puzzle(day=8, year=2022)
    forest = Forest(puzzle.input_data)
    print(forest.visible_trees())
    print(forest.max_scenic_score())


if __name__ == "__main__":
    main()
