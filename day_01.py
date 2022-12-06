"""Day 1: Calorie Counting."""
from aocd.models import Puzzle


class Elfs:
    """Elfs carrying food."""

    def __init__(self) -> None:
        """Initiate class."""
        self.elfs: list[int] = []

    def add_data(self, elf_input: str) -> None:
        """Add info about each elf and how much food they are carrying."""
        # Split input on double line breaks which separates each elf
        elfs_data = elf_input.split("\n\n")

        # Split each food calory count, convert to int and sum it up
        self.elfs = [sum(map(int, x.splitlines())) for x in elfs_data]

    def get_total_calories(self) -> int:
        """Return the total calories of the elf with most calories."""
        return max(self.elfs)

    def get_total_calories_top_3(self) -> int:
        """Return the total calories of the top 3 elfs with most calories."""
        return sum(sorted(self.elfs)[-3:])


def main() -> None:
    """Solve the puzzle."""
    puzzle = Puzzle(day=1, year=2022)
    elfs = Elfs()
    elfs.add_data(puzzle.input_data)
    print(elfs.get_total_calories())
    print(elfs.get_total_calories_top_3())


if __name__ == "__main__":
    main()
