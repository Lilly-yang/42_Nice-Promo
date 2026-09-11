import numpy as np
import copy


class MazeGenerator:
    def __init__(self, width, height, seed):
        """
        width  → maze width
        height → maze height
        seed   → random seed
        """
        self.width = width
        self.height = height
        self.seed = seed
        self.creat_maze()

    def creat_maze(self):
        self.maze = []
        for _ in range(self.height):
            row_tmp = []
            for _ in range(self.width):
                cell = {
                    "N": 1,
                    "E": 1,
                    "S": 1,
                    "W": 1
                }
                row_tmp.append(cell)
            self.maze.append(row_tmp)

    def _get_neighbors(self, x, y):
        nbs = []
        if x - 1 >= 0:
            nbs.append((x-1, y))

        if x + 1 < self.width:
            nbs.append((x+1, y))

        if y - 1 >= 0:
            nbs.append((x, y-1))

        if y + 1 < self.height:
            nbs.append((x, y+1))

        return nbs


    def generate(self):
        self.maze = 

    def get_maze():
        return self.maze

    def save_structe():

    def get_solution():
