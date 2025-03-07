import random
from array2d import Array2D 
import copy
import time
import os
from projects.project2.kbhit import KBHit

LIVE_CELL = '🦠'
EMPTY_CELL = ' '

class GameOfLife:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = Array2D.empty(rows, cols, str)
        self.scratch_grid = Array2D.empty(rows, cols, str)
        self.history = []

    def seed_grid(self, random_seed: bool = True, config_file: str = None):
        if random_seed:
            for row in range(self.rows):
                for col in range(self.cols):
                    self.grid[row][col] = LIVE_CELL if random.random() < 0.5 else EMPTY_CELL
        else:
            self.load_configuration(config_file)

    def load_configuration(self, config_file: str):
        with open(config_file, 'r') as file:
            lines = file.readlines()
            for row, line in enumerate(lines):
                for col, char in enumerate(line.strip()):
                    self.grid[row][col] = char

    def count_neighbors(self, row: int, col: int) -> int:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                count += self.grid[r][c] == LIVE_CELL
        return count

    def compute_next_generation(self):
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = self.count_neighbors(row, col)
                if self.grid[row][col] == LIVE_CELL:
                    if neighbors < 2 or neighbors > 3:
                        self.scratch_grid[row][col] = EMPTY_CELL
                    else:
                        self.scratch_grid[row][col] = LIVE_CELL
                else:
                    if neighbors == 3:
                        self.scratch_grid[row][col] = LIVE_CELL
                    else:
                        self.scratch_grid[row][col] = EMPTY_CELL

    def update_grid(self):
        self.grid = copy.deepcopy(self.scratch_grid)

    def display_grid(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(str(self.grid))

    def run_simulation(self, mode: str):
        kb = KBHit()
        while True:
            self.display_grid()
            self.compute_next_generation()
            self.update_grid()
            self.history.append(copy.deepcopy(self.grid))

            if len(self.history) > 5:
                self.history.pop(0)
            if len(self.history) >= 2 and self.history[-1] == self.history[-2]:
                print("Stable configuration detected. Simulation ends.")
                break

            if mode == 'automatic':
                time.sleep(1)
            elif mode == 'manual':
                while True:
                    if kb.kbhit():
                        key = kb.getch()
                        if key == 'M':
                            mode = 'manual'
                            break
                        elif key == 'A':
                            mode = 'automatic'
                            break
                        elif key == 'Q':
                            return

def main():
    rows, cols = 10, 10
    game = GameOfLife(rows, cols)
    start_option = input("Enter 'R' for random start, or 'F' for file input: ").upper()
    if start_option == 'R':
        game.seed_grid(random_seed=True)
    elif start_option == 'F':
        config_file = input("Enter configuration file name: ")
        game.seed_grid(random_seed=False, config_file=config_file)
    
    mode = input("Enter 'A' for automatic mode, 'M' for manual mode: ").lower()
    game.run_simulation(mode)

if __name__ == "__main__":
    main()
