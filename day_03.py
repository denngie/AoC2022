"""Day 3: Rucksack Reorganization."""
from aocd.models import Puzzle


class Rucksacks:
    """Rucksacks with supplies."""

    def __init__(self, content_list: str) -> None:
        """Initiate class."""
        self.rucksacks: list[str] = content_list.splitlines()

    def find_common(self) -> int:
        """Calculate priority for the common item in each rucksack."""
        priority_sum = 0
        for rucksack in self.rucksacks:
            half = int(len(rucksack) / 2)
            common_item = set(rucksack[:half]).intersection(rucksack[half:]).pop()
            offset = 38 if ord(common_item) < 97 else 96  # lowercase gets offset 96, uppercase 38
            priority_sum += ord(common_item) - offset
        return priority_sum

    def find_badge(self) -> int:
        """Split rucksacks into groups of 3 and find intersection of each group."""
        priority_sum = 0
        for i in range(0, len(self.rucksacks), 3):
            badge = set.intersection(*map(set, self.rucksacks[i:i + 3])).pop()
            offset = 38 if ord(badge) < 97 else 96  # lowercase gets offset 96, uppercase 38
            priority_sum += ord(badge) - offset
        return priority_sum


def main() -> None:
    """Solve the puzzle."""
    puzzle = Puzzle(day=3, year=2022)
    rucksacks = Rucksacks(puzzle.input_data)
    print(rucksacks.find_common())
    print(rucksacks.find_badge())


if __name__ == "__main__":
    main()
