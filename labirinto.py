def main():
    rows, cols, obstacles = map(int, input().split())

    board = []
    obstacle_count = 0

    for _ in range(rows):
        row = input().replace('.', 'X')
        obstacle_count += row.count('#')
        board.append(list(row))

    empty_cells = (rows * cols) - obstacles - obstacle_count

    fill_empty_cells(board, rows, cols, empty_cells)

    print_board(board)


def fill_empty_cells(board, rows, cols, empty_cells):
    empty_positions = []

    for i in range(rows):
        if 'X' in board[i]:
            j = board[i].index('X')
            board[i][j] = '.'
            empty_positions = [(i, j)]
            empty_cells -= 1
            break

    while empty_cells:
        x, y = empty_positions.pop()
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and board[new_x][new_y] == 'X':
                board[new_x][new_y] = '.'
                empty_positions.append((new_x, new_y))
                empty_cells -= 1
                if empty_cells == 0:
                    break


def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end="")
        print()


main()
