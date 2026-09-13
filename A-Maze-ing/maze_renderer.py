from mazegen import MazeGenerator


class MazeRenderer:
    def __init__(self, maze: list,
                 generator: MazeGenerator,
                 solution: list = [],
                 show_solution: bool = True) -> None:
        self.maze = maze
        self.solution = solution
        self.show_solution = show_solution
        self.generator = generator
        self.reset: str = "\033[0m"
        self.wall_color: str = "\033[31m"
        self.color_index = 0
        self.icon_cell = generator.icon_cell

    def _change_wall_color(self) -> None:
        colors = [
            "\033[31m",  # red
            "\033[32m",  # green
            "\033[34m",  # blue
            "\033[35m",  # magenta
            "\033[36m",  # cyan
        ]

        self.color_index = (self.color_index + 1) % len(colors)
        self.wall_color = colors[self.color_index]

    def display(self) -> None:
        self._draw_tob(0, "N")

        for row in range(len(self.maze)):
            self._draw_middle(row)
            self._draw_tob(row, "S")

    def _draw_tob(self, row: int, tob: str) -> None:
        line = "+"

        for cell in self.maze[row]:
            if cell[tob]:
                line += "---+"
            else:
                line += "   +"

        print(self._wall(line))

    def _draw_middle(self, row: int, solution: str = "") -> None:
        line = self._wall("|")

        for colum, cell in enumerate(self.maze[row]):
            w_h = (colum, row)
            if w_h in self.icon_cell:
                incert = "#"
            elif self.show_solution and w_h in self.solution:
                ind = self.solution.index((colum, row))
                incert = "\033[33m" + self._solution_icon(ind) + self.reset
            else:
                incert = " "

            line += self._draw_middle_cell(cell, incert)

        print(line)

    def _wall(self, text: str) -> str:
        return self.wall_color + text + self.reset

    def _draw_middle_cell(self, cell: dict, incert: str) -> str:
        line: str = " " + incert + " "
        if cell["E"]:
            return line + self._wall("|")
        else:
            return line + " "

    def _solution_icon(self, ind: int) -> str:
        if ind == 0:
            return "S"

        if ind == len(self.solution) - 1:
            return "E"

        return "*"

    def toggle_solution(self) -> None:
        self.show_solution = not self.show_solution

    def run(self) -> None:
        self.display()

        while True:
            command = input(
                "Command (R: regenerate maze, S: show/hide solution, "
                "C: change color, Q: quit): "
                )

            if command.upper() == "S":
                self.toggle_solution()
                self.display()

            elif command.upper() == "Q":
                break

            elif command.upper() == "R":
                self.maze = self.generator.generate_maze()
                self.solution = self.generator.solve()
                self.display()

            elif command.upper() == "C":
                self._change_wall_color()
                self.display()
