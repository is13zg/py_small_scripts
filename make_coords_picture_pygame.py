import pygame
import sys


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for x in range(self.left, self.width * self.cell_size + self.left, self.cell_size):
            for y in range(self.top, self.height * self.cell_size + self.top, self.cell_size):
                pygame.draw.rect(screen, (0, 0, 0), (x, y, self.cell_size, self.cell_size), 1)
        pygame.display.flip()

    def paint(self, x, y, color):
        x = x - 1
        y = 10 - y
        pygame.draw.rect(screen, pygame.Color(color), (
            self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size), 0)
        pygame.display.flip()


wdth, hght = 600, 600

pygame.init()
screen = pygame.display.set_mode((wdth, hght))
screen.fill((0, 0, 0))

board = Board(10, 10)
board.set_view(20, 20, 50)
screen.fill((255, 255, 255))
board.render()

data = list(map(str.strip, sys.stdin))
for ex in data:
    try:
        x = int(ex.split("X")[0])
        y = int(ex.split("X")[1].split("=")[0])
        clr = ex.split("(")[1].split(")")[0]
        board.paint(x, y, clr)
    except:
        print("EX  Error", ex)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
