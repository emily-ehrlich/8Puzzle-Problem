import random
import numpy as np

from Board import Board

# set goal matrix as this should not change, only the starting matrix changes
GOAL_MATRIX = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]


# generate the starting metrix with values 0-8, where 0 represents the "blank space" in the puzzle
def generate_metrix():
    boundaries = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(boundaries)
    start_matrix = np.array(boundaries).reshape(3, 3)

    return start_matrix


class Puzzle:
    # Initialize the puzzle
    def __init__(self):
        self.size = 3
        self.open = []
        self.close = []

    # use the heuristic function to calc value of f(x) = h(x) + g(x)
    def calc_heuristic(self, m_start, m_goal):
        return self.difference(m_start.data, m_goal) + m_start.level

    # calculates the difference between the stating and goal matrices
    def difference(self, start_data, goal_data):
        diff = 0
        for i in range(0, self.size):
            for j in range(0, self.size):
                if start_data[i][j] != goal_data[i][j] and start_data[i][j] != 0:
                    diff += 1
        return diff

    def process(self):
        start_matrix = generate_metrix()

        start_matrix = Board(start_matrix, 0, 0)
        start_matrix.final = self.calc_heuristic(start_matrix, GOAL_MATRIX)

        # place starting board in the open list
        self.open.append(start_matrix)
        print("START")
        while True:
            current = self.open[0]
            print("*--------*")
            for i in current.data:
                print("| ", end="")
                for j in i:
                    print(j, end=" ")
                print("|", end="")
                print()
            print("*--------*")

            # when the difference has reached 0 then we have reached the final goal state
            print("CALC: " + str(self.difference(current.data, GOAL_MATRIX)))
            if self.difference(current.data, GOAL_MATRIX) == 0:
                break

            children = current.generate_children()
            for i in children:
                i.final = self.calc_heuristic(i, GOAL_MATRIX)
                self.open.append(i)
            self.close.append(current)
            del self.open[0]

            self.open.sort(key=lambda x: x.final, reverse=False)


Puzzle().process()
