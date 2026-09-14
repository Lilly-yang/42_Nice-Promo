import random
import sys
from itertools import cycle


class MazeGenerator:
    def __init__(self,
                 width: int,
                 height: int,
                 entry: tuple,
                 exit: tuple,
                 perfect: bool = True,
                 output_file: str = "maze.txt",
                 seed: int | None = None,
                 icon42: bool = True) -> None:
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        self.output_file = output_file
        self.seed = seed
        self.icon42 = icon42
        self.solution: list[tuple] = []
        self.icon_cell: set[tuple] = set()

    def _init_maze(self) -> None:
        self.maze = []
        for _ in range(0, self.height):
            row_tmp = []
            for _ in range(0, self.width):
                cell = {
                    "N": 1,
                    "E": 1,
                    "S": 1,
                    "W": 1
                }
                row_tmp.append(cell)
            self.maze.append(row_tmp)

        print(f"maze initiated: width - {self.width}, height - {self.height}")

        if self.width < 9 or self.height < 7:
            self.icon42 = False
            print("Error: 42 pattern is omitted because maze is too small!")

        if self.icon42:
            w = int(self.width / 2) - 3
            h = int(self.height / 2) - 2
            self._get_icon_cell(w, h)

        if self.entry in self.icon_cell or self.exit in self.icon_cell:
            self.icon42 = False
            self.icon_cell.clear()
            print("Error: 42 pattern is omitter "
                  "because cell is occupied with entry or exit!")

    def _get_icon_cell(self, offset_w: int, offset_h: int) -> None:
        init_icon_cell = [(0, 0), (0, 1), (0, 2),
                          (1, 2),
                          (2, 2), (2, 3), (2, 4),
                          (4, 0), (4, 2), (4, 3), (4, 4),
                          (5, 0), (5, 2), (5, 4),
                          (6, 0), (6, 1), (6, 2), (6, 4)]

        self.icon_cell = set(
            [(w+offset_w, h+offset_h) for w, h in init_icon_cell]
            )

    def generate_maze(self) -> list:
        self._init_maze()
        self.rng = random.Random(self.seed)
        print("maze generating...")
        visited = set()
        stack = []

        start = self.entry
        stack.append(start)
        visited.add(start)
        while True:
            neighbors = self._get_neighbors(start[0], start[1])
            valid_nb = neighbors - visited
            if valid_nb:
                next_cell = self.rng.choice(sorted(valid_nb))
                self._remove_wall(start, next_cell)
                start = next_cell
                stack.append(start)
                visited.add(start)
            else:
                stack.pop()
                if stack:
                    start = stack[-1]
                else:
                    break

        print("---*perfect maze generated*---")

        if not self.perfect:
            print("non-perfect maze...")
            self._loop_gen()
            print("---non-perfect maze generated---")

        return self.maze

    def _get_neighbors(self, w: int, h: int) -> set:
        nbs = set()
        if w - 1 >= 0:
            nbs.add((w-1, h))

        if w + 1 < self.width:
            nbs.add((w+1, h))

        if h - 1 >= 0:
            nbs.add((w, h-1))

        if h + 1 < self.height:
            nbs.add((w, h+1))

        return nbs - self.icon_cell

    def _remove_wall(self, str: tuple, nxt: tuple) -> None:
        str_w, str_h = str
        end_w, end_h = nxt

        if str_h == end_h:
            if str_w > end_w:
                self.maze[str_h][str_w]["W"] = 0
                self.maze[end_h][end_w]["E"] = 0
            else:
                self.maze[str_h][str_w]["E"] = 0
                self.maze[end_h][end_w]["W"] = 0

        if str_w == end_w:
            if str_h > end_h:
                self.maze[str_h][str_w]["N"] = 0
                self.maze[end_h][end_w]["S"] = 0
            else:
                self.maze[str_h][str_w]["S"] = 0
                self.maze[end_h][end_w]["N"] = 0

    def _loop_gen(self) -> None:
        dead_ends = self._get_dead_ends()
        dead_ends_before = -1
        dead_ends_now = len(dead_ends)
        open_drc = cycle(["SE", "NW"])

        while dead_ends_now > 2 and dead_ends_now != dead_ends_before:
            print(f"dead ends: {len(dead_ends)}")

            dead_ends_before = dead_ends_now
            n = int(dead_ends_now / 2) + 1
            candidate = self._get_cell_to_open(dead_ends, next(open_drc))

            for _ in range(n):
                if not candidate:
                    break

                h, w, drc = self.rng.choice(candidate)
                candidate.remove((h, w, drc))

                self.maze[h][w][drc] = 0

                if drc == "S":
                    self.maze[h+1][w]["N"] = 0

                if drc == "E":
                    self.maze[h][w+1]["W"] = 0

                if drc == "N":
                    self.maze[h-1][w]["S"] = 0

                if drc == "W":
                    self.maze[h][w-1]["E"] = 0

            dead_ends = self._get_dead_ends()
            dead_ends_now = len(dead_ends)

        print(f"finale dead ends: {dead_ends_now}")

    def _get_cell_to_open(self,
                          org_cells: list,
                          direction: str = "SE") -> list:
        # print(f"---getting cells that avaliable to open {direction}---")
        candidate = []

        if direction == "SE":
            for w, h in org_cells:
                if (
                    h < self.height - 1
                    and (w, h+1) not in self.icon_cell
                    and self.maze[h][w]["S"] == 1
                ):
                    candidate.append((h, w, "S"))
                if (
                    w < self.width - 1
                    and (w+1, h) not in self.icon_cell
                    and self.maze[h][w]["E"] == 1
                ):
                    candidate.append((h, w, "E"))

        if direction == "NW":
            for w, h in org_cells:
                if (
                    h
                    and (w, h-1) not in self.icon_cell
                    and self.maze[h][w]["N"] == 1
                ):
                    candidate.append((h, w, "N"))
                if (
                    w
                    and (w-1, h) not in self.icon_cell
                    and self.maze[h][w]["W"] == 1
                ):
                    candidate.append((h, w, "W"))

        return candidate

    def _get_dead_ends(self) -> list:
        dead_ends = []

        for h in range(self.height):
            for w in range(self.width):
                if (w, h) in self.icon_cell:
                    continue

                open_count = 0

                for direction in ["N", "E", "S", "W"]:
                    if self.maze[h][w][direction] == 0:
                        open_count += 1

                if open_count == 1:
                    dead_ends.append((w, h))

        return dead_ends

    def solve(self) -> list:
        print("solving maze...")
        visited = set()
        stack = []
        # solution = []

        start = self.entry
        stack.append(start)
        visited.add(start)
        while True:
            if start == self.exit:
                self.solution = stack
                # print(f"maze solved: {''.join(solution[:10])}", end="")
                # if len(solution) > 10:
                #     print("...")
                return stack

            neighbors = self._get_open_neighbors(start[0], start[1])
            valid_nb = neighbors - visited
            if valid_nb:
                start = self.rng.choice(sorted(valid_nb))
                # solution.append(self._get_direction(start, next_cell))
                # start = next_cell
                stack.append(start)
                visited.add(start)
            else:
                stack.pop()
                # solution.pop()
                if stack:
                    start = stack[-1]
                else:
                    break

        print("Solve maze failed!")
        sys.exit(1)
        return []

    def _get_open_neighbors(self, w: int, h: int) -> set:
        nbs = set()

        if not self.maze[h][w]["N"] and h > 0:
            nbs.add((w, h-1))

        if not self.maze[h][w]["S"] and h < self.height-1:
            nbs.add((w, h+1))

        if not self.maze[h][w]["W"] and w > 0:
            nbs.add((w-1, h))

        if not self.maze[h][w]["E"] and w < self.width-1:
            nbs.add((w+1, h))

        return nbs

    def _get_direction(self, cell_list: list) -> str:
        direction = ""
        for i in range(0, len(cell_list)-1):
            str_w, str_h = cell_list[i]
            end_w, end_h = cell_list[i+1]

            if str_h == end_h:
                if str_w > end_w:
                    direction += "W"
                else:
                    direction += "E"

            if str_w == end_w:
                if str_h > end_h:
                    direction += "N"
                else:
                    direction += "S"
        print(f"solution: {direction[:10]}", end="")
        if len(direction) > 10:
            print("...")
        return direction

    def output_maze(self) -> None:
        from pathlib import Path
        current_dir = Path(__file__).resolve().parent.parent
        output_path = current_dir / self.output_file
        with open(output_path, "w") as f:
            for h in range(self.height):
                line = ""
                for w in range(self.width):
                    line += self._direction_hexadecimal(self.maze[h][w])
                f.write(line + "\n")

            f.write('\n')
            f.write(str(self.entry[0])+","+str(self.entry[1])+"\n")
            f.write(str(self.exit[0])+","+str(self.exit[1])+"\n")
            if not len(self.solution):
                self.solution = self.solve()
            f.write(self._get_direction(self.solution)+"\n")

        print(f"maze saved in: {output_path}")

    def _direction_hexadecimal(self, cell: dict) -> str:
        dec_cell = (
            cell["N"]
            + cell["E"] * 2
            + cell["S"] * 4
            + cell["W"] * 8
        )

        # dec_cell = 0
        # for ind, drc in enumerate(["W", "S", "E", "N"]):
        #     dec_cell += cell[drc] * (2 ** ind)

        hex_digits = "0123456789ABCDEF"
        return hex_digits[dec_cell]
