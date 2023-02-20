class Board:
    # Initialize the node with the data, level of the node and the calculated final value
    def __init__(self, data, level, final):
        self.data = data
        self.level = level
        self.final = final

    # children are generated when the the blank position "0" is moved in any of the
    # following directions: up (U), down (D), left (L), right (r)
    def generate_children(self):
        x, y = self.find(self.data, 0)
        # initiate the possible directions to move,
        directions = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
        children = []
        for i in directions:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_position = Board(child, self.level+1, 0)
                children.append(child_position)
        return children

    # In this method we moved the "blank" in the direction given and if this puts the
    # blank position outside the board then we return none
    def shuffle(self, pos, x1, y1, x2, y2):
        if 0 <= x2 < len(self.data) and 0 <= y2 < len(self.data):
            # calculate the new position as a possibility
            temp_pos = self.copy(pos)
            temp = temp_pos[x2][y2]
            temp_pos[x2][y2] = temp_pos[x1][y1]
            temp_pos[x1][y1] = temp
            return temp_pos
        else:
            return None

    # TODO: See if I actually need this
#         copy the metrix into a similar metrix
    def copy(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

#     used to find the position of the "blank space" or 0
    def find(self, pos, x):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if pos[i][j] == x:
                    return i, j

