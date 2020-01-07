import numpy
from PIL import Image
import timeit


def process_numpy():
    grid = numpy.zeros((5000, 5000), dtype=numpy.int8)
    for x in range(0, 5000):
        for y in range(0, 5000):
            grid[x, y] = (x // 38 + y // 38)
    Image.fromarray(grid).show()
    print('Completed!')


def process_pil():
    grid = Image.new(mode="L", size=(5000, 5000))
    for x in range(0, 5000):
        for y in range(0, 5000):
            grid.putpixel((x, y), (x // 38 + y // 38))
    grid.show()
    print('Completed!')


if __name__ == '__main__':
    print('PIL - Time spent: ', timeit.timeit(lambda: process_pil(), number=10), 's')
    print('numpy - Time spent: ', timeit.timeit(lambda: process_numpy(), number=10), 's')
