"""Day 5: Supply Stacks."""
from aocd.models import Puzzle


class Crates:
    """Crates full of supplies."""

    def __init__(self, crates_drawing: str) -> None:
        """Initiate class."""
        self.crates_drawing = crates_drawing
        self.moves: list[str] = []
        self.stacks: list[list[str]]
        self._interpret_drawing()

    def _interpret_drawing(self) -> None:
        """Interpret drawing as vertical lists of each stack."""
        drawing_lines = self.crates_drawing.splitlines()
        number_of_stacks = int((len(drawing_lines[0]) + 1) / 4)  # First line length reveals number
        self.stacks = [[] for x in range(number_of_stacks)]

        for line_number, line in enumerate(drawing_lines):
            if line[1] == "1":
                self.moves = drawing_lines[line_number + 2:]  # Moves start two lines after
                break

            for i in range(number_of_stacks):
                # 4 * i + 1 equals crate position for each stack
                if line[4 * i + 1] != " ":  # If not empty, add crate to start of crate list
                    self.stacks[i].insert(0, line[4 * i + 1])

    def calculate_moves_9000(self) -> str:
        """Move crates - CrateMover 9000."""
        for move in self.moves:
            _, amount, _, source, _, dest = move.split(maxsplit=6)  # Ignore the words of each move
            for _ in range(int(amount)):
                crate = self.stacks[int(source) - 1].pop()  # Get and remove crate from source stack
                self.stacks[int(dest) - 1].append(crate)  # Add crate to dest stack

        return "".join([stack[-1] for stack in self.stacks])  # Get top crates from each stack

    def calculate_moves_9001(self) -> str:
        """Move crates - CrateMover 9001."""
        self._interpret_drawing()  # Reset stacks according to drawing again
        for move in self.moves:
            _, amount, _, source, _, dest = move.split(maxsplit=6)  # Ignore the words of each move
            crates_to_move = self.stacks[int(source) - 1][-int(amount):]  # Get last n of crate(s)
            del self.stacks[int(source) - 1][-int(amount):]  # Delete crate(s) from source stack
            self.stacks[int(dest) - 1] += crates_to_move  # Add crate(s) to dest stack

        return "".join([stack[-1] for stack in self.stacks])  # Get top crates from each stack


def main() -> None:
    """Solve the puzzle."""
    puzzle = Puzzle(day=5, year=2022)
    crates = Crates(puzzle.input_data)
    print(crates.calculate_moves_9000())
    print(crates.calculate_moves_9001())


if __name__ == "__main__":
    main()
