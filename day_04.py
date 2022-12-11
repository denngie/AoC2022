"""Day 4: Camp Cleanup."""
from aocd.models import Puzzle


class Camp:
    """Camp with cleanup sections."""

    def __init__(self, content_list: str) -> None:
        """Initiate class."""
        self.cleaning_assignments: list[str] = content_list.splitlines()

    def _elf_sections(self, elfs_input: str) -> list[list[int]]:
        """Split elf jobs and return expanded list."""
        elfs = elfs_input.split(",")
        elf_sections = []
        for i in range(0, 2):
            start, end = elfs[i].split("-", 1)
            elf_sections.append(list(range(int(start), int(end) + 1)))

        return elf_sections

    def find_job_overlaps(self) -> int:
        """Find number of overlapping jobs between elfs in each assignment."""
        overlaps = 0
        for assignment in self.cleaning_assignments:
            elf_sections = self._elf_sections(assignment)
            if (set(elf_sections[0]).issubset(elf_sections[1])
               or set(elf_sections[1]).issubset(elf_sections[0])):
                overlaps += 1

        return overlaps

    def find_section_overlaps(self) -> int:
        """Find number of overlapping sections between elfs in each assignment."""
        overlaps = 0
        for assignment in self.cleaning_assignments:
            elf_sections = self._elf_sections(assignment)
            if not set(elf_sections[0]).isdisjoint(elf_sections[1]):
                overlaps += 1

        return overlaps


def main() -> None:
    """Solve the puzzle."""
    puzzle = Puzzle(day=4, year=2022)
    camp = Camp(puzzle.input_data)
    print(camp.find_job_overlaps())
    print(camp.find_section_overlaps())


if __name__ == "__main__":
    main()
