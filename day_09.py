"""Day 9: Rope Bridge."""
from aocd.models import Puzzle


class Bridge:
    """Rope bridge."""

    def __init__(self, motion: str) -> None:
        """Initiate class."""
        self.motion = motion.splitlines()
        self.knots: list[list[int]] = []
        self.tail_visited: list[tuple] = []

    def _reset(self) -> None:
        """Reset knots and tail_visited."""
        self.knots = []
        self.tail_visited = []

    def _move(self, move: str) -> None:
        """Move head and tail."""
        if move == "R":
            self.knots[0][0] += 1
        elif move == "U":
            self.knots[0][1] += 1
        elif move == "L":
            self.knots[0][0] -= 1
        elif move == "D":
            self.knots[0][1] -= 1
        for i in range(1, len(self.knots)):
            head = self.knots[i - 1]
            tail = self.knots[i]

            diff_x = head[0] - tail[0]
            diff_y = head[1] - tail[1]

            if not (abs(diff_x) <= 1 and abs(diff_y) <= 1):
                if diff_x != 0:
                    tail[0] += int(abs(diff_x) / diff_x)
                if diff_y != 0:
                    tail[1] += int(abs(diff_y) / diff_y)

        if tuple(self.knots[-1]) not in self.tail_visited:
            self.tail_visited.append(tuple(self.knots[-1]))

    def positions_visited(self, length: int) -> int:
        """Calculate all of the positions the tail visited at least once."""
        self._reset()
        for _ in range(length):
            self.knots.append([0, 0])

        for move in self.motion:
            direction, steps = move.split()
            for _ in range(int(steps)):
                self._move(direction)

        return len(self.tail_visited)


def main() -> None:
    """Solve the puzzle."""
    puzzle = Puzzle(day=9, year=2022)
    bridge = Bridge(puzzle.input_data)
    print(bridge.positions_visited(2))
    print(bridge.positions_visited(10))


if __name__ == "__main__":
    main()
