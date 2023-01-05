"""Day 7: No Space Left On Device."""
from aocd.models import Puzzle


class Node:
    """Simple parent child object."""

    def __init__(self, name: str, parent: str) -> None:
        """Initiate class."""
        self.parent = parent
        self.child: list[str] = []
        self.name = name
        self.total_size = 0


class Filesystem:
    """Filesystem full of directories and files."""

    def __init__(self, terminal_output: str) -> None:
        """Initiate class."""
        self.terminal_output = terminal_output
        self.dirs: dict = {}
        self._parse_terminal_output()

    def _parse_terminal_output(self) -> None:
        """Interpret terminal output and build dirs dict."""
        for line in self.terminal_output.splitlines():
            if line[0] == "$":
                if line[2:4] == "cd":
                    if line[5:] == "/":
                        node = Node("/", "")
                        self.dirs[node.name] = node
                    elif line[5:] == "..":
                        size = node.total_size
                        node = self.dirs[node.parent]
                        node.total_size += size
                    else:
                        node.child.append(line[5:])
                        node = Node(node.name + line[5:], node.name)
                        self.dirs[node.name] = node
                elif line[2:4] == "ls":
                    pass
            else:
                if line[0:3] == "dir":
                    pass
                else:
                    node.total_size += int(line.split()[0])

        # After last line we need to update all the parents size
        while node.parent != "":
            size = node.total_size
            node = self.dirs[node.parent]
            node.total_size += size

    def small_dirs(self) -> int:
        """Find directories with a total size of at most 100000."""
        sum_of_sizes = 0
        for node in self.dirs.values():
            if node.total_size <= 100000:
                sum_of_sizes += node.total_size
        return sum_of_sizes

    def smallest_dir_to_delete(self) -> int:
        """Return dir size of the smallest directory which frees up enough space."""
        size_needed = self.dirs["/"].total_size - 40000000
        big_node_sizes = []
        for node in self.dirs.values():
            if node.total_size > size_needed:
                big_node_sizes.append(node.total_size)
        big_node_sizes.sort()
        return big_node_sizes[0]


def main() -> None:
    """Solve the puzzle."""
    puzzle = Puzzle(day=7, year=2022)
    filesystem = Filesystem(puzzle.input_data)
    print(filesystem.small_dirs())
    print(filesystem.smallest_dir_to_delete())


if __name__ == "__main__":
    main()
