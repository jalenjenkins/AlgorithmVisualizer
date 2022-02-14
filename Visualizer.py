import pygame
import random
pygame.init()


class DrawingLogistics:

    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREY = 138, 128, 128
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND = WHITE

    GRADIENTS = [
        GREY,
        (160, 160, 160),
        (192, 192, 192)
    ]

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, arr):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(arr)

    def set_list(self, arr):
        self.arr = arr

        self.min_val = min(arr)
        self.max_val = max(arr)

        self.block_width = round((self.width - self.SIDE_PAD) / len(arr))
        self.block_height = {
            round((self.height - self.TOP_PAD) /
                  (self.max_val - self.min_val))
        }

        self.start_x = self.SIDE_PAD // 2


def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND)
    pygame.display.update()


def draw_arr(draw_info):
    arr = draw_info.arr
    for i, val in enumerate(arr):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - ((val - draw_info.min_val)
                                * draw_info.block_height)


def generate_list(n, min_val, max_val):
    arr = []
    for _ in range(n):
        arr.append(random.randint(min_val, max_val))
    return arr


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 5
    max_val = 200

    new_arr = generate_list(n, min_val, max_val)
    draw_info = DrawingLogistics(800, 600, new_arr)
    draw(draw_info)
    pygame.display.update()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


if __name__ == "__main__":
    main()
