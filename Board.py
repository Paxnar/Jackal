from TilesClasses import *
import random


class Board:
    def __init__(self, mode: int):
        if mode == 0:
            self.board = [[Sea()] + [0 for _ in range(11)] + [Sea()] for _ in range(13)]
            self.board[0] = [Sea() for _ in range(13)]
            self.board[-1] = [Sea() for _ in range(13)]
            self.board[1][0] = Sea()
            self.board[1][-1] = Sea()
            self.board[1] = [Sea(), Sea()] + [0] * 9 + [Sea(), Sea()]
            self.board[-2] = [Sea(), Sea()] + [0] * 9 + [Sea(), Sea()]
            possible_tiles = make_possible_tiles(mode)
            for o in range(len(self.board)):
                for p in range(len(self.board[o])):
                    if self.board[o][p] == 0:
                        ch = random.choice(possible_tiles)
                        possible_tiles.remove(ch)
                        self.board[o][p] = UTile(ch)

    def reveal_tile(self, tile):
        if isinstance(tile, UTile):
            return tile.tile
        return tile

    def show_board_like_list(self):
        for i in self.board:
            print(i)

    def get_cell(self, mouse_pos):
        mx = mouse_pos[0]
        my = mouse_pos[1]
        return [my // 76, mx // 76]
