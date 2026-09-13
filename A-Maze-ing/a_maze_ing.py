from mazegen import MazeGenerator
import sys
from maze_renderer import MazeRenderer
from typing import TypedDict
from typing_extensions import NotRequired


class Config(TypedDict, total=False):
    WIDTH: int
    HEIGHT: int
    ENTRY: tuple[int, int]
    EXIT: tuple[int, int]
    OUTPUT_FILE: str
    PERFECT: bool
    SEED: NotRequired[int | None]
    # ALGORITHM: str
    # DISPLAY_MODE: str


def read_config(filename: str) -> Config:
    config: Config = {}

    with open(filename) as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)
            if key == "WIDTH":
                config["WIDTH"] = int(value)
            elif key == "HEIGHT":
                config["HEIGHT"] = int(value)
            elif key == "SEED":
                config["SEED"] = int(value)
            elif key == "ENTRY":
                config["ENTRY"] = parse_coordinates(value)
            elif key == "EXIT":
                config["EXIT"] = parse_coordinates(value)
            elif key == "PERFECT":
                config["PERFECT"] = value == "True"
            elif key == "OUTPUT_FILE":
                config["OUTPUT_FILE"] = value

    for cfg in ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]:
        if cfg not in config:
            print(f"Config must contain {cfg}")
            sys.exit(1)

    return config


def parse_coordinates(value: str) -> tuple[int, int]:
    x, y = value.split(",")
    return int(x), int(y)


def display(maze: list, solution: list, generator: MazeGenerator) -> None:
    rendor = MazeRenderer(maze, generator, solution)
    rendor.run()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze-ing.py <config_file>")
        sys.exit(1)

    config_file = sys.argv[1]
    config = read_config(config_file)
    print(f"---config readed---\n{config}")

    generator = MazeGenerator(
        width=config["WIDTH"],
        height=config["HEIGHT"],
        entry=config["ENTRY"],
        exit=config["EXIT"],
        output_file=config["OUTPUT_FILE"],
        perfect=config["PERFECT"],
        )
    maze = generator.generate_maze()
    solution = generator.solve()
    generator.output_maze()
    display(maze, solution, generator)
