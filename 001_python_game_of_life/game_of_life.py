# programming the game of life in python
import random
import time

# The Game of Life is a cellular automaton devised by the mathematician John Horton Conway.
# It consists of a grid of cells that can be in one of two states: alive (1) or dead (0).
# The state of each cell in the next generation is determined by the current state of its neighbors according to the following rules:
# 1. Any live cell with fewer than 2 live neighbors dies (underpopulation).
# 2. Any live cell with 2 or 3 live neighbors lives on to the next generation.
# 3. Any live cell with more than 3 live neighbors dies (overpopulation).
# 4. Any dead cell with exactly 3 live neighbors becomes alive (reproduction).

def random_state(rows, cols, alive_probability=0.3):
    """Generate a random state for the Game of Life starting with a dead state."""
    state = dead_state(rows, cols)
    for i in range(rows):
        for j in range(cols):
            # Randomly set some cells to alive (1) or keep them dead (0) with probability
            if random.random() < alive_probability:
                state[i][j] = 1
            else:
                state[i][j] = 0
            
    return state

def dead_state(rows, cols):
    """Generate a dead state for the Game of Life."""
    return [[0 for _ in range(cols)] for _ in range(rows)]

def render(state):
    """Render the state of the Game of Life in the terminal."""
    for row in state:
        print(' '.join(['█' if cell == 1 else ' ' for cell in row]))

def next_state(state):
    """Compute the next state of the Game of Life based on the current state."""
    rows, cols = len(state), len(state[0])
    new_state = dead_state(rows, cols)
    
    for i in range(rows):
        for j in range(cols):
            # Count alive neighbors
            alive_neighbors = sum(
                state[i + di][j + dj]
                for di in [-1, 0, 1]
                for dj in [-1, 0, 1]
                if (di != 0 or dj != 0) and (0 <= i + di < rows) and (0 <= j + dj < cols)
            )
            
            # Apply Game of Life rules
            if state[i][j] == 1:  # Current cell is alive
                if alive_neighbors < 2:
                    new_state[i][j] = 0  # Underpopulation
                elif alive_neighbors in [2, 3]:
                    new_state[i][j] = 1  # Lives on to the next generation
                else:
                    new_state[i][j] = 0  # Overpopulation
            else:  # Current cell is dead
                if alive_neighbors == 3:
                    new_state[i][j] = 1  # Reproduction
    
    return new_state

width, height = 20, 20
state = random_state(height, width)

while True:
    state = next_state(state)
    print("\033[H\033[J", end="")  # Clear the terminal
    render(state)
    time.sleep(0.5)  # Pause for a moment before the next update