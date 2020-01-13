import matplotlib.pyplot as plt
import numpy


if __name__ == '__main__':
    grid = numpy.zeros((256, 256))
    for x in range(0, 255):
        for y in range(0, 255):
            grid[x, y] = (x // 2 + y // 2)
    plt.figure()
    imgplot = plt.imshow(grid)
    plt.colorbar()
