import random


def greeting():
    print('                **    **  ********  **        **            **      ')
    print("               **    **  ********  **        **         **     **   ")
    print("              ********  **        **        **         **      **  ")
    print("             ********  ********  **        **         **      **  ")
    print("            **    **  **        **        **         **      **  ")
    print("           **    **  ********  ********  ********    **    **   ")
    print("          **    **  ********  ********  ********       **      ")
    print("Приветствую вас в игре ,,Сапёр''*")
    print('* Made by MasIT')
    print('''Сапёр — известная игра-головоломка для одного игрока на прямоугольном поле.''')
    print('''В некоторых точках поля расположены мины. Цель игрока — открыть все клетки, на которых мин нет,''')
    print('''причём нажатие на мину означает мгновенный проигрыш.''')
    print()


def level_choose():
    print('Выберите желаемый уровень игры:')
    print('1 уровень «Новичок» доске 9x9 с 10 минами')
    print('2 уровень «НовичокPro» доске 8x8 с 10 минами')
    print('3 уровень «Промежуточный» доске 16x16 с 40 минами')
    print('4 уровень «Эксперт» доске 30x16 с 99 минами')
    print()
    print('Наберите 1, 2, 3 или 4')
    while (choose_level := input().strip()) not in ['1', '2', '3', '4']:
        print('Наберите 1, 2, 3 или 4')
    print()
    print('Отлично, идём дальше!')
    return int(choose_level)


def rules_motion():
    print('Ваш ход должен выглядеть так:')
    print('[номер ряда] [номер ячейки] [действия]')
    print('Список возможных действий с ячейками поля:')
    print('F - флажок, указывающий на предполагаемое положение мины, нельзя открыть клетку, не сняв его')
    print('? - вопросительный знак, указывающий на предполагаемое положение мины, нельзя открыть клетку, не сняв его')
    print('O - открыть клетку')
    print('T - снимает знак или флажок с клетки')


use_cords_open_empty_cells = []


def open_neighborhood_empty_cells(real_field_, game_field_, motion_row, motion_col):
    global use_cords_open_empty_cells
    game_field_[motion_row][motion_col] = '   '
    use_cords_open_empty_cells.append([motion_row, motion_col])

    # расположение в (0, 0)
    if not motion_row and not motion_col:
        game_field_[motion_row][motion_col + 1] = real_field_[motion_row][motion_col + 1]
        game_field_[motion_row + 1][motion_col] = real_field_[motion_row + 1][motion_col]
        game_field_[motion_row + 1][motion_col + 1] = real_field_[motion_row + 1][motion_col + 1]

        if real_field_[motion_row][motion_col + 1] == '   ' and [motion_row, motion_col + 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row, motion_col + 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row, motion_col + 1)
        if real_field_[motion_row + 1][motion_col] == '   ' and [motion_row + 1][motion_col] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row + 1, motion_col])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row + 1, motion_col)
        if real_field_[motion_row + 1][motion_col + 1] == '   ' and [motion_row + 1][motion_col + 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row + 1, motion_col + 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row + 1, motion_col + 1)
        return game_field_

    # расположение в (motion_row - 1, 0)
    elif motion_row == len(real_field_) - 1 and not motion_col:
        game_field_[motion_row][motion_col + 1] = real_field_[motion_row][motion_col + 1]
        game_field_[motion_row - 1][motion_col] = real_field_[motion_row - 1][motion_col]
        game_field_[motion_row - 1][motion_col + 1] = real_field_[motion_row - 1][motion_col + 1]

        if real_field_[motion_row][motion_col + 1] == '   ' and [motion_row, motion_col + 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row, motion_col + 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row, motion_col + 1)
        if real_field_[motion_row - 1][motion_col] == '   ' and [motion_row - 1, motion_col] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row - 1, motion_col])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row - 1, motion_col)
        if real_field_[motion_row - 1][motion_col + 1] == '   ' and [motion_row - 1, motion_col + 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row - 1, motion_col + 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row - 1, motion_col + 1)
        return game_field_

    # расположение в (motion_row - 1, motion_col - 1)
    elif motion_row == len(real_field_) - 1 and motion_col == len(real_field_[0]) - 1:
        game_field_[motion_row][motion_col - 1] = real_field_[motion_row][motion_col - 1]
        game_field_[motion_row - 1][motion_col] = real_field_[motion_row - 1][motion_col]
        game_field_[motion_row - 1][motion_col - 1] = real_field_[motion_row - 1][motion_col - 1]

        if real_field_[motion_row][motion_col - 1] == '   ' and [motion_row, motion_col - 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row, motion_col - 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row, motion_col - 1)
        if real_field_[motion_row - 1][motion_col] == '   ' and [motion_row - 1, motion_col] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row - 1, motion_col])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row - 1, motion_col)
        if real_field_[motion_row - 1][motion_col - 1] == '   ' and [motion_row - 1, motion_col - 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row - 1, motion_col - 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row - 1, motion_col - 1)
        return game_field_

    # расположение в (0, motion_col - 1)
    elif not motion_row and motion_col == len(real_field_[0]) - 1:
        game_field_[motion_row][motion_col - 1] = real_field_[motion_row][motion_col - 1]
        game_field_[motion_row + 1][motion_col] = real_field_[motion_row + 1][motion_col]
        game_field_[motion_row + 1][motion_col - 1] = real_field_[motion_row + 1][motion_col - 1]

        if real_field_[motion_row][motion_col - 1] == '   ' and [motion_row, motion_col - 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row, motion_col - 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row, motion_col - 1)
        if real_field_[motion_row + 1][motion_col] == '   ' and [motion_row + 1, motion_col] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row + 1, motion_col])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row + 1, motion_col)
        if real_field_[motion_row + 1][motion_col - 1] == '   ' and [motion_row + 1, motion_col - 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row + 1, motion_col - 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row + 1, motion_col - 1)
        return game_field_

    # расположение в верхней стороне
    elif not motion_row:
        game_field_[motion_row][motion_col - 1] = real_field_[motion_row][motion_col - 1]
        game_field_[motion_row][motion_col + 1] = real_field_[motion_row][motion_col + 1]
        game_field_[motion_row + 1][motion_col - 1] = real_field_[motion_row + 1][motion_col - 1]
        game_field_[motion_row + 1][motion_col] = real_field_[motion_row + 1][motion_col]
        game_field_[motion_row + 1][motion_col + 1] = real_field_[motion_row + 1][motion_col + 1]

        if real_field_[motion_row][motion_col - 1] == '   ' and [motion_row, motion_col - 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row, motion_col - 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row, motion_col - 1)
        if real_field_[motion_row][motion_col + 1] == '   ' and [motion_row, motion_col + 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row, motion_col + 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row, motion_col + 1)
        if real_field_[motion_row + 1][motion_col - 1] == '   ' and [motion_row + 1, motion_col - 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row + 1, motion_col - 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row + 1, motion_col - 1)
        if real_field_[motion_row + 1][motion_col] == '   ' and [motion_row + 1, motion_col] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row + 1, motion_col])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row + 1, motion_col)
        if real_field_[motion_row + 1][motion_col + 1] == '   ' and [motion_row + 1, motion_col + 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row + 1, motion_col + 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row + 1, motion_col + 1)
        return game_field_

    # расположение в нижней стороне
    elif motion_row == len(real_field_) - 1:
        game_field_[motion_row][motion_col - 1] = real_field_[motion_row][motion_col - 1]
        game_field_[motion_row][motion_col + 1] = real_field_[motion_row][motion_col + 1]
        game_field_[motion_row - 1][motion_col - 1] = real_field_[motion_row - 1][motion_col - 1]
        game_field_[motion_row - 1][motion_col] = real_field_[motion_row - 1][motion_col]
        game_field_[motion_row - 1][motion_col + 1] = real_field_[motion_row - 1][motion_col + 1]

        if real_field_[motion_row][motion_col - 1] == '   ' and [motion_row, motion_col - 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row, motion_col - 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row, motion_col - 1)
        if real_field_[motion_row][motion_col + 1] == '   ' and [motion_row, motion_col + 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row, motion_col + 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row, motion_col + 1)
        if real_field_[motion_row - 1][motion_col - 1] == '   ' and [motion_row - 1, motion_col - 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row - 1, motion_col - 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row - 1, motion_col - 1)
        if real_field_[motion_row - 1][motion_col] == '   ' and [motion_row - 1, motion_col] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row - 1, motion_col])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row - 1, motion_col)
        if real_field_[motion_row - 1][motion_col + 1] == '   ' and [motion_row - 1, motion_col + 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row - 1, motion_col + 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row - 1, motion_col + 1)
        return game_field_

    # расположение в левой стороне
    elif not motion_col:
        game_field_[motion_row - 1][motion_col] = real_field_[motion_row - 1][motion_col]
        game_field_[motion_row + 1][motion_col] = real_field_[motion_row + 1][motion_col]
        game_field_[motion_row - 1][motion_col + 1] = real_field_[motion_row - 1][motion_col + 1]
        game_field_[motion_row][motion_col + 1] = real_field_[motion_row][motion_col + 1]
        game_field_[motion_row + 1][motion_col + 1] = real_field_[motion_row + 1][motion_col + 1]

        if real_field_[motion_row - 1][motion_col] == '   ' and [motion_row - 1, motion_col] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row - 1, motion_col])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row - 1, motion_col)
        if real_field_[motion_row + 1][motion_col] == '   ' and [motion_row + 1, motion_col] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row + 1, motion_col])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row + 1, motion_col)
        if real_field_[motion_row - 1][motion_col + 1] == '   ' and [motion_row - 1, motion_col + 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row - 1, motion_col + 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row - 1, motion_col + 1)
        if real_field_[motion_row][motion_col + 1] == '   ' and [motion_row, motion_col + 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row, motion_col + 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row, motion_col + 1)
        if real_field_[motion_row + 1][motion_col + 1] == '   ' and [motion_row + 1, motion_col + 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row + 1, motion_col + 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row + 1, motion_col + 1)
        return game_field_

    # расположение в правой стороне
    elif motion_col == len(real_field_[0]) - 1:
        game_field_[motion_row - 1][motion_col] = real_field_[motion_row - 1][motion_col]
        game_field_[motion_row + 1][motion_col] = real_field_[motion_row + 1][motion_col]
        game_field_[motion_row - 1][motion_col - 1] = real_field_[motion_row - 1][motion_col - 1]
        game_field_[motion_row][motion_col - 1] = real_field_[motion_row][motion_col - 1]
        game_field_[motion_row + 1][motion_col - 1] = real_field_[motion_row + 1][motion_col - 1]

        if real_field_[motion_row - 1][motion_col] == '   ' and [motion_row - 1, motion_col] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row - 1, motion_col])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row - 1, motion_col)
        if real_field_[motion_row + 1][motion_col] == '   ' and [motion_row + 1, motion_col] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row + 1, motion_col])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row + 1, motion_col)
        if real_field_[motion_row - 1][motion_col - 1] == '   ' and [motion_row - 1, motion_col - 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row - 1, motion_col - 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row - 1, motion_col - 1)
        if real_field_[motion_row][motion_col - 1] == '   ' and [motion_row, motion_col - 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row, motion_col - 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row, motion_col - 1)
        if real_field_[motion_row + 1][motion_col - 1] == '   ' and [motion_row + 1, motion_col - 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row + 1, motion_col - 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row + 1, motion_col - 1)
        return game_field_

    # расположение не в периметре(все 8 соседей)
    else:
        game_field_[motion_row - 1][motion_col - 1] = real_field_[motion_row - 1][motion_col - 1]
        game_field_[motion_row - 1][motion_col] = real_field_[motion_row - 1][motion_col]
        game_field_[motion_row - 1][motion_col + 1] = real_field_[motion_row - 1][motion_col + 1]
        game_field_[motion_row][motion_col - 1] = real_field_[motion_row][motion_col - 1]
        game_field_[motion_row][motion_col + 1] = real_field_[motion_row][motion_col + 1]
        game_field_[motion_row + 1][motion_col - 1] = real_field_[motion_row + 1][motion_col - 1]
        game_field_[motion_row + 1][motion_col] = real_field_[motion_row + 1][motion_col]
        game_field_[motion_row + 1][motion_col + 1] = real_field_[motion_row + 1][motion_col + 1]

        if real_field_[motion_row - 1][motion_col - 1] == '   ' and [motion_row - 1, motion_col - 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row - 1, motion_col - 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row - 1, motion_col - 1)
        if real_field_[motion_row - 1][motion_col] == '   ' and [motion_row - 1, motion_col] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row - 1, motion_col])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row - 1, motion_col)
        if real_field_[motion_row - 1][motion_col + 1] == '   ' and [motion_row - 1, motion_col + 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row - 1, motion_col + 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row - 1, motion_col + 1)
        if real_field_[motion_row][motion_col - 1] == '   ' and [motion_row, motion_col - 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row, motion_col - 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row, motion_col - 1)
        if real_field_[motion_row][motion_col + 1] == '   ' and [motion_row, motion_col + 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row, motion_col + 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row, motion_col + 1)
        if real_field_[motion_row + 1][motion_col - 1] == '   ' and [motion_row + 1, motion_col - 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row + 1, motion_col - 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row + 1, motion_col - 1)
        if real_field_[motion_row + 1][motion_col] == '   ' and [motion_row + 1, motion_col] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row + 1, motion_col])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row + 1, motion_col)
        if real_field_[motion_row + 1][motion_col + 1] == ' ' and [motion_row + 1, motion_col + 1] not in \
                use_cords_open_empty_cells:
            use_cords_open_empty_cells.append([motion_row + 1, motion_col + 1])
            open_neighborhood_empty_cells(real_field_, game_field_, motion_row + 1, motion_col + 1)
        return game_field_


def open_neighborhood_mines(real_field_, game_field_, motion_row, motion_col):
    for i in range(len(real_field_)):
        for j in range(len(real_field_[i])):
            if real_field_[i][j] == ' * ':
                game_field_[i][j] = ' * '

    return game_field_


def generate_field(game_field, mines_quality, rows_quality, columns_quality, cannot_flag, cannot_row=0, cannot_col=0):
    """функция, генерирующая поле, * - означает мину, пустая ячейка - среди соседей нет мин,
    цифры - количество мин среди соседей, cannot_flag, cannot_row, cannot_col - флаг и координаты, которые будут
    перестраивать поле, если игрок при первом же ходе выбрал мину"""
    field = game_field[:]

    # создаём мины
    for _ in range(mines_quality):
        random_row = random.randrange(rows_quality)
        random_col = random.randrange(columns_quality)

        if cannot_flag:
            while field[random_row][random_col] == ' * ' or (random_row == cannot_row and random_col == cannot_col):
                random_row = random.randrange(rows_quality)
                random_col = random.randrange(columns_quality)
        else:
            while field[random_row][random_col] == ' * ':
                random_row = random.randrange(rows_quality)
                random_col = random.randrange(columns_quality)

        field[random_row][random_col] = ' * '

    # считаем количество мин среди соседей
    for i in range(rows_quality):
        for j in range(columns_quality):
            if field[i][j] != ' * ':
                cnt = 0
                # расположение в (0, 0)
                if not i and not j:
                    if field[i][j + 1] == ' * ':
                        cnt += 1
                    if field[i + 1][j] == ' * ':
                        cnt += 1
                    if field[i + 1][j + 1] == ' * ':
                        cnt += 1

                # расположение в (rows_quality - 1, 0)
                elif i == rows_quality - 1 and not j:
                    if field[i][j + 1] == ' * ':
                        cnt += 1
                    if field[i - 1][j] == ' * ':
                        cnt += 1
                    if field[i - 1][j + 1] == ' * ':
                        cnt += 1

                # расположение в (rows_quality - 1, columns_quality - 1)
                elif i == rows_quality - 1 and j == columns_quality - 1:
                    if field[i][j - 1] == ' * ':
                        cnt += 1
                    if field[i - 1][j] == ' * ':
                        cnt += 1
                    if field[i - 1][j - 1] == ' * ':
                        cnt += 1

                # расположение в (0, columns_quality - 1)
                elif not i and j == columns_quality - 1:
                    if field[i][j - 1] == ' * ':
                        cnt += 1
                    if field[i + 1][j] == ' * ':
                        cnt += 1
                    if field[i + 1][j - 1] == ' * ':
                        cnt += 1

                # расположение в верхней стороне
                elif not i:
                    if field[i][j - 1] == ' * ':
                        cnt += 1
                    if field[i][j + 1] == ' * ':
                        cnt += 1
                    if field[i + 1][j - 1] == ' * ':
                        cnt += 1
                    if field[i + 1][j] == ' * ':
                        cnt += 1
                    if field[i + 1][j + 1] == ' * ':
                        cnt += 1

                # расположение в нижней стороне
                elif i == rows_quality - 1:
                    if field[i][j - 1] == ' * ':
                        cnt += 1
                    if field[i][j + 1] == ' * ':
                        cnt += 1
                    if field[i - 1][j - 1] == ' * ':
                        cnt += 1
                    if field[i - 1][j] == ' * ':
                        cnt += 1
                    if field[i - 1][j + 1] == ' * ':
                        cnt += 1

                # расположение в левой стороне
                elif not j:
                    if field[i - 1][j] == ' * ':
                        cnt += 1
                    if field[i + 1][j] == ' * ':
                        cnt += 1
                    if field[i - 1][j + 1] == ' * ':
                        cnt += 1
                    if field[i][j + 1] == ' * ':
                        cnt += 1
                    if field[i + 1][j + 1] == ' * ':
                        cnt += 1

                # расположение в правой стороне
                elif j == columns_quality - 1:
                    if field[i - 1][j] == ' * ':
                        cnt += 1
                    if field[i + 1][j] == ' * ':
                        cnt += 1
                    if field[i - 1][j - 1] == ' * ':
                        cnt += 1
                    if field[i][j - 1] == ' * ':
                        cnt += 1
                    if field[i + 1][j - 1] == ' * ':
                        cnt += 1

                # расположение не в периметре(все 8 соседей)
                else:
                    if field[i - 1][j - 1] == ' * ':
                        cnt += 1
                    if field[i - 1][j] == ' * ':
                        cnt += 1
                    if field[i - 1][j + 1] == ' * ':
                        cnt += 1
                    if field[i][j - 1] == ' * ':
                        cnt += 1
                    if field[i][j + 1] == ' * ':
                        cnt += 1
                    if field[i + 1][j - 1] == ' * ':
                        cnt += 1
                    if field[i + 1][j] == ' * ':
                        cnt += 1
                    if field[i + 1][j + 1] == ' * ':
                        cnt += 1

                # устанавливаем количество соседей - мин
                if not cnt:
                    field[i][j] = '   '
                else:
                    field[i][j] = ' ' + str(cnt) + ' '

    return field


def game():
    # приветствие
    greeting()

    # выбор уровня
    level = level_choose()
    if level == 1:
        rows, columns, mines = 9, 9, 10
    elif level == 2:
        rows, columns, mines = 8, 8, 10
    elif level == 3:
        rows, columns, mines = 16, 16, 40
    else:
        rows, columns, mines = 16, 30, 99

    # поле с расстановкой
    real_field = generate_field([['[ ]' for _ in range(columns)] for _ in range(rows)],
                                mines, rows, columns, False)

    # создаём поле, которое видит пользователь
    field_view = [['[ ]' for _ in range(columns)] for _ in range(rows)]

    # знакомство с правилами хода
    rules_motion()

    print('Начнём игру!')

    # основной цикл игры
    first_motion = True
    while True:
        print()
        print(*[' '.join(str(i) for i in el) for el in field_view], sep='\n')
        print('Делайте ход')
        while not ((motion := input()) and len(motion.split()) == 3 and motion.split()[0].isdigit() and
                   motion.split()[1].isdigit() and 0 < int(motion.split()[0]) <= rows and
                   0 < int(motion.split()[1]) <= columns and motion.split()[2] in ['?', 'F', 'O', 'T']):
            rules_motion()

        motion = [int(motion.split()[0]) - 1, int(motion.split()[1]) - 1, motion.split()[2]]
        if motion[2] == '?':
            if field_view[motion[0]][motion[1]] == '[ ]':
                field_view[motion[0]][motion[1]] = '[?]'
            elif field_view[motion[0]][motion[1]] == '[?]':
                print('Вы уже поставили в эту клетку вопросительный знак!')
            elif field_view[motion[0]][motion[1]] == '[F]':
                print('Вы уже поставили в эту клетку флаг!')
            else:
                print('Вы уже открыли эту ячейку!')
        elif motion[2] == 'F':
            if field_view[motion[0]][motion[1]] == '[ ]':
                field_view[motion[0]][motion[1]] = '[F]'
            elif field_view[motion[0]][motion[1]] == '[?]':
                print('Вы уже поставили в эту клетку вопросительный знак!')
            elif field_view[motion[0]][motion[1]] == '[F]':
                print('Вы уже поставили в эту клетку флаг!')
            else:
                print('Вы уже открыли эту ячейку!')
        elif motion[2] == 'T':
            if field_view[motion[0]][motion[1]] in ['[?]', '[F]']:
                field_view[motion[0]][motion[1]] = '[ ]'
            if field_view[motion[0]][motion[1]] != '[ ]':
                print('Вы уже открыли эту ячейку!')
            else:
                print('С этой клетки нечего снимать!')
        else:
            if field_view[motion[0]][motion[1]] == '[ ]':
                if real_field[motion[0]][motion[1]] != ' * ':
                    if real_field[motion[0]][motion[1]] != '   ':
                        field_view[motion[0]][motion[1]] = real_field[motion[0]][motion[1]]
                    else:
                        field_view = open_neighborhood_empty_cells(real_field, field_view, motion[0], motion[1])
                else:
                    if first_motion:
                        real_field = generate_field(field_view, mines, rows, columns, True, motion[0],
                                                    motion[1])
                        if real_field[motion[0]][motion[1]] != ' ':
                            field_view[motion[0]][motion[1]] = real_field[motion[0]][motion[1]]
                        else:
                            field_view = open_neighborhood_empty_cells(real_field, field_view, motion[0], motion[1])
                    else:
                        field_view = open_neighborhood_mines(real_field, field_view, motion[0], motion[1])
                        print(*[' '.join([str(j) for j in i]) for i in field_view], sep='\n')
                        print('Вы проиграли, попробуйте ещё раз!')
                        break
            elif field_view[motion[0]][motion[1]] not in ['[?]', '[F]']:
                print('Вы уже открыли эту ячейку!')
            else:
                if field_view[motion[0]][motion[1]] == '[?]':
                    print('Сначала снимите вопросительный знак с клетки')
                else:
                    print('Сначала снимите флажок с клетки')

        first_motion = False

        # проверка на ситуацию выиграл ли игрок
        win = True
        for i in range(len(field_view)):
            for j in range(len(field_view[i])):
                if field_view[i][j] in ['[F]', '[?]', '[ ]'] and real_field[i][j] != '*':
                    win = False
                    break
            if not win:
                break
        if win:
            print(*[' '.join(str(i) for i in el) for el in field_view], sep='\n')
            print('Поздравляю! Вы выиграли!')
            break
    final()


def final():
    print("Желаете сыграть ещё раз?) ('да' или 'нет')")
    while (answer := input()).lower().strip() not in ['да', 'нет']:
        print('Некорректный ответ!')
        print("Желаете сыграть ещё раз?) ('да' или 'нет')")
    if answer == 'да':
        game()
    else:
        print('Оцените игру от 0 до 10')
        while not (mark := input()).strip().isdigit() and 0 <= int(mark) <= 10:
            print('Некорректный ответ!')
            print('Оцените игру от 0 до 10')
        print('Спасибо за оценку')
        print('Будем рады видеть Вас ещё!')
        print('До свиданья!*')
        print('* Made by MasIT')


game()
