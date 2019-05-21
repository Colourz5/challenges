class board:
    def __init__(self):
        column_empty = "......"
        board_empty = [list(column_empty),
                       list(column_empty),
                       list(column_empty),
                       list(column_empty),
                       list(column_empty),
                       list(column_empty),
                       list(column_empty)]
        self.game_state = board_empty
        turns = 0
        for column in self.game_state:
            turns += column.count(".")
        self.turns_left = turns
        self.last_spot = (None, None)
        self.last_player = None

    def drop_counter(self, column, player):
        if "." in self.game_state[column]:
            row = self.game_state[column].index(".")
            turns = 0
            for col in self.game_state:
                turns += col.count(".")
            self.game_state[column][row] = player
            self.turns_left = turns
            self.last_spot = (column, row)
            self.last_player = player
        else:
            raise ValueError("Column is already full!")

    def display(self):
        for column in self.game_state:
            print("".join(column))

    def winner(self):
        player = self.last_player
        # horizontal and vertical win checking
        column_index, row_index = self.last_spot
        row = []
        for col in range(len(self.game_state)):
            row.append(self.game_state[col][row_index])
        column = "".join(self.game_state[column_index])
        row = "".join(row)
        winning = 4*player
        if winning in column:
            return True
        elif winning in row:
            return True
        # diagonal checking \ only if root spot is [0, 3] is it possible
        # diagonal checking / only if root spot is [., 6] is it possible
        # getting the root spot HARDCODED (assuming board is 6 rows x 7 columns)
        else:
            if column_index - row_index >= 0:
                root = ((column_index - row_index), 0)
                # diagonal checking \ only if root spot is [0, 3] is it possible
                if root[0] >= 0 and root[0] <= 3:
                    diagonal = []
                    # only works if column length is shorter than row length
                    for i in range(len(row) - root[0] - 1):
                        entry = self.game_state[root[0] + i][root[1] + i]
                        diagonal.append(entry)
                    diagonal = "".join(diagonal)
                    if winning in diagonal:
                        print(diagonal, "in the \\ direction")
                        return True
                # diagonal checking / only if root spot is [., 6] is it possible
                if root[0] >= 3 and root[0] <= 6:
                    diagonal = []
                    print(root[0])
                    for i in range(root[0]):
                        print("This is the column {} and this is the row {}".format(root[0] - i, root[1] + i))
                        entry = self.game_state[root[0] - i][root[1] + i]
                        diagonal.append(entry)
                    # issue the root is assuming you want the winning direction to be \ direction, look at excel to see
                    print(diagonal, "in the / direction")
                    if winning in diagonal:
                        print(diagonal, "in the / direction")
                        return True
            else:
                root = ((column_index - row_index + 5), len(column) - 1)
        return False


def play():
    players = ["R", "Y"]
    game_board = board()
    turn = 0
    while game_board.turns_left > 0:
        player = players[turn % 2]
        column = int(input("Which column do you want to play in? "))
        try:
            game_board.drop_counter(column, player)
        except ValueError as v:
            print(v)
            game_board.display()
            print("{} available moves left".format(game_board.turns_left))
            continue
        game_board.display()
        print("{} available moves left".format(game_board.turns_left))
        turn += 1
        if game_board.winner():
            break
    print(player, "won!")


if __name__ == "__main__":
    play()
