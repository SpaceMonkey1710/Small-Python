ROW_LENGTH = 3
ROWS_COUNT = 3

field = [['_' for _ in range(ROW_LENGTH)] for _ in range(ROWS_COUNT)]
iter_number = 1


def render_field():
    for row in field:
        print(row)


def move(current_figure, coords):
    if field[coords[0]][coords[1]] == '_':
        field[coords[0]][coords[1]] = current_figure
    else:
        wrong_move(current_figure, coords)


def wrong_move(current_figure, coords):
    print('В это поле нельзя ходить')
    print(f'Ходит {current_figure}:')
    coords = [int(c) - 1 for c in input()]
    move(current_figure, coords)


def end_of_game(coords):
    pass


while True:
    render_field()

    if iter_number % 2:
        current_figure = 'X'
    else:
        current_figure = 'O'
    iter_number += 1
    print(f'Ходит {current_figure}:')
    coords = [int(c) - 1 for c in input()]

    move(current_figure, coords)
