from pokeclone import characters
from pokeclone.board import Board, Cell

if __name__ == '__main__':
    print("Welcome to PokeClone!")
    board = Board(5, 6)
    player = characters.initialize_player()
    board[3][3] = Cell("T")
    while True:
        print(player)
        print(board)
        valid_move = False
        while not valid_move:
            new_offset = player.move()
            valid_move = board.update_player_pos(new_offset)
