"""Day 6: Tuning Trouble."""
from aocd.models import Puzzle


class Device:
    """Crates full of supplies."""

    def __init__(self, datastream: str) -> None:
        """Initiate class."""
        self.datastream = datastream

    def find_marker(self, marker_type: str) -> int:
        """Find first marker where the characters are all unique."""
        if marker_type == "message":
            seq = 14
        elif marker_type == "packet":
            seq = 4

        for pos in range(seq, len(self.datastream)):
            if len(set(self.datastream[pos - seq:pos])) == len(self.datastream[pos - seq:pos]):
                return pos

        return False


def main() -> None:
    """Solve the puzzle."""
    puzzle = Puzzle(day=6, year=2022)
    device = Device(puzzle.input_data)
    print(device.find_marker("packet"))
    print(device.find_marker("message"))


if __name__ == "__main__":
    main()
