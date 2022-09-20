from Board import Board
from TilesClasses import *
running = True
all_sprites = pygame.sprite.Group()

if __name__ == '__main__':
    pygame.init()
    size = width, height = 988, 988
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    all_sprites = pygame.sprite.Group()

    board = Board(0)
    board.show_board_like_list()

    for row in range(len(board.board)):
        for col in range(len(board.board[row])):
            board.board[row][col].rect.x = 76 * col
            board.board[row][col].rect.y = 76 * row
            all_sprites.add(board.board[row][col])
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for row in range(len(board.board)):
                for col in range(len(board.board[row])):
                    screen.blit(board.board[row][col].image, board.board[row][col].rect)
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cellcords = board.get_cell(event.pos)
                all_sprites.remove(board.board[cellcords[0]][cellcords[1]])
                board.board[cellcords[0]][cellcords[1]] = board.reveal_tile(board.board[cellcords[0]][cellcords[1]])
                board.board[cellcords[0]][cellcords[1]].rect.x = 76 * cellcords[1]
                board.board[cellcords[0]][cellcords[1]].rect.y = 76 * cellcords[0]
                all_sprites.add(board.board[cellcords[0]][cellcords[1]])

    # завершение работы:
    pygame.quit()
