import pygame
import random
import math
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

    FONT = pygame.font.SysFont("times new roman", 20)
    LARGER_FONT = pygame.font.SysFont("times new roman", 30)
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
        self.block_height = math.floor(
            (self.height - self.TOP_PAD) / (self.max_val - self.min_val))

        self.start_x = self.SIDE_PAD // 2


def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND)

    controls = draw_info.FONT.render(
        "R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending",
        1, draw_info.BLACK)
    draw_info.window.blit(
        controls, (draw_info.width/2 - controls.get_width()/2, 5))

    sorting = draw_info.FONT.render(
        "I - Insertion Sort | B - Bubble Sort | M - Merge Sort",
        1, draw_info.BLACK)
    draw_info.window.blit(
        sorting, (draw_info.width/2 - sorting.get_width()/2, 35))

    draw_arr(draw_info)
    pygame.display.update()


def draw_arr(draw_info, color_positions={}, clear_background=False):
    arr = draw_info.arr

    if clear_background:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND, clear_rect)

    for i, val in enumerate(arr):
        x = draw_info.start_x + i * draw_info.block_width
        y = (draw_info.height - (val - draw_info.min_val) *
             draw_info.block_height)

        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color,
                         (x, y, draw_info.block_width, draw_info.height))

    if clear_background:
        pygame.display.update()


def generate_list(n, min_val, max_val):
    arr = []
    for _ in range(n):
        arr.append(random.randint(min_val, max_val))
    return arr


def bubble_sort(draw_info, ascending=True):
    arr = draw_info.arr

    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            num1 = arr[j]
            num2 = arr[j+1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw_arr(draw_info, {j: draw_info.GREEN, j +
                         1: draw_info.RED}, clear_background=True)
                yield True
    return arr


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 5
    max_val = 200

    new_arr = generate_list(n, min_val, max_val)
    draw_info = DrawingLogistics(800, 600, new_arr)
    sorting = False
    ascending = True
    current_algo = bubble_sort
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info)

        draw(draw_info)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                new_arr = generate_list(n, min_val, max_val)
                draw_info.set_list(new_arr)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = current_algo(
                    draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            # elif event.key == pygame.K_b:
            #     current_algo = bubble_sort
            # elif event.key == pygame.K_b :
            #     current_algo = merge_sort
            # elif event.key == pygame.K_b :
            #     current_algo = insert_sort
    pygame.quit()


if __name__ == "__main__":
    main()
