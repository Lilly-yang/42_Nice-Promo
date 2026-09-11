from ..mazegen import MazeGenerator


if __name__ == "__main__":
    generator = MazeGenerator()
    generator.generate()
    maze = generator.get_maze()
    solution = generator.get_solution()
