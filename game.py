
import pygame
import sys # установка библиотек


def check_win(mas, sign): # проверяет наличие выигрышной комбинации на игровом поле
    zeroes = 0
    for row in mas: # цикл проходит по всем строкам и проверяет сколько раз встречается переменная sign
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3): # цикл проходит по всем столбцам и проверяет сколько раз встречается переменная sign
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign: # проверяет диагонали
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeroes == 0: # если все ячейки заняты, но ни одно условие выше не выполняется - ничья
        return 'НИЧЬЯ'
    return False


def doska(): # функция которая создает доску и позволяет играть
    pygame.init() # команда, которая запускает pygame
    size_block = 150 # устанавливаем размер блока
    margin = 30 #размер отступов
    width = heigth = size_block * 3 + margin * 4 #длина и ширина доски

    size_window = (width, heigth) #
    screen = pygame.display.set_mode(size_window) # создает окно в pygame с заданными шириной и высотой
    pygame.display.set_caption('крестики нолики') #передается строка, которую функция устанавливает в качестве заголовка окна

    black = (0, 0, 0) # выбор цвета
    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)
    mas = [[0] * 3 for i in range(3)] # создание массива из трех строк и трех столбцов, который заполнен нулями
    query = 0 #номер хода
    game_over = False

    while True: # создание бесконечного цикла
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Если произошло событие «QUIT» (например, закрытие окна)
                pygame.quit() #отключает (деинициализирует) pygame
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over: #Если нажата кнопка мыши и игра не окончена
                x_mouse, y_mouse = pygame.mouse.get_pos() # определяются координаты мыши
                col = x_mouse // (size_block + margin)  # Вычисляется столбец и строка для размещения знака
                row = y_mouse // (size_block + margin)
                if mas[col][row] == 0: # если ячейка пустая
                    if query % 2: # если номер хода четный, в ячейку ставится крестик
                        mas[col][row] = 'x'
                    else:
                        mas[col][row] = 'o' # если номер хода нечетный, в ячейку ставится нолик
                    query += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #Если нажата клавиша «Пробел», игра начинается заново
                game_over = False #Установка значения переменной game_over в False
                mas = [[0] * 3 for i in range(3)] #Создание двумерного списка mas размером 3x3, заполненного нулями.
                query = 0 #Установка переменной query в 0
                screen.fill(black) #Очистка экрана (заливка цветом black).

        if not game_over:
            for row in range(3): #В цикле перебираются все ячейки игрового поля по строкам и столбцам
                for col in range(3):
                    if mas[col][row] == 'x': # если в ячейке крестик - ячейка становится красной
                        color = red
                    elif mas[col][row] == 'o': # если в ячейке ноль - ячейка становится зеленой
                        color = green
                    else:
                        color = white  # иначе ячейка белого цвета
                    x = col * size_block + (col + 1) * margin
                    y = row * size_block + (row + 1) * margin
                    pygame.draw.rect(screen, color, (x, y, size_block, size_block)) #отрисовка ячеек игрового поля
                    if color == red: # Если ячейка содержит крестик, то рисуется крестик белого цвета
                        pygame.draw.line(screen, white, (x, y), (x + size_block, y + size_block), 4)
                        pygame.draw.line(screen, white, (x + size_block, y), (x, y + size_block), 4)
                    elif color == green: #Если ячейка содержит нолик, то рисуется круг белого цвета
                        pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2),
                                           size_block // 2 - 2, 4)
        if (query - 1) % 2 == 0: # если номер хода нечетный
            game_over = check_win(mas, 'o') #переменной game_over присваивается результат функции check_win(mas, 'o')
        else:
            game_over = check_win(mas, 'x') #о переменной game_over присваивается результат функции check_win(mas, 'x')
        if game_over:
            screen.fill(black) # экран заполняется черным цветом
            font = pygame.font.SysFont('stxingkai', 90) #создается шрифт размером 90
            text1 = font.render(game_over, True, white)
            text_rect = text1.get_rect()
            text_x = screen.get_height() / 2 - text_rect.width / 2 # вычисляются координаты, чтобы текст находился по центру экрана
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text1, [text_x, text_y]) #текст рисуется по этим координатам

        pygame.display.update() #отображение изменений на экране


doska()
