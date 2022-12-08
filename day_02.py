"""Day 2: Rock Paper Scissors."""
from aocd.models import Puzzle


class RPS:
    """Rock Paper Scissors."""

    def __init__(self, strategy_guide: str) -> None:
        """Initiate class."""
        self.strategy: list[list[str]]
        self._add_data(strategy_guide)

    def _add_data(self, strategy_guide: str) -> None:
        """Add moves from strategy guide."""
        self.strategy = [x.split(" ") for x in strategy_guide.splitlines()]

    def total_score(self) -> int:
        """Calculate total score."""
        score = 0
        for game in self.strategy:
            score += ord(game[1]) - 87  # 1 for Rock, 2 for Paper, and 3 for Scissors
            if ((game[1] == "X" and game[0] == "C")      # Rock beats scissors
               or (game[1] == "Y" and game[0] == "A")    # Paper beats rock
               or (game[1] == "Z" and game[0] == "B")):  # Scissor beats paper
                score += 6
            elif ord(game[1]) == ord(game[0]) + 23:  # Draw
                score += 3
            else:  # Loss
                continue

        return score

    def correct_score(self) -> int:
        """Calculate correct score."""
        game_rules = {"C": {"win": 1, "lose": 2},  # Rock beats scissors
                      "A": {"win": 2, "lose": 3},  # Paper beats rock
                      "B": {"win": 3, "lose": 1}}  # Scissor beats paper

        score = 0
        for game in self.strategy:
            if game[1] == "X":  # Lose
                score += game_rules[game[0]]["lose"]
            elif game[1] == "Y":  # Draw
                score += 3
                score += ord(game[0]) - 64
            elif game[1] == "Z":  # Win
                score += 6
                score += game_rules[game[0]]["win"]

        return score


def main() -> None:
    """Solve the puzzle."""
    puzzle = Puzzle(day=2, year=2022)
    rps = RPS(puzzle.input_data)
    print(rps.total_score())
    print(rps.correct_score())


if __name__ == "__main__":
    main()
