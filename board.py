import matplotlib.pyplot as plt
import numpy as np


def show(pixel_array, board_description=""):
    plt.ion()
    boundaries = [0, len(pixel_array), 0, len(pixel_array)]
    img = plt.imshow(pixel_array, extent=boundaries)
    img.set_cmap('Greys')
    plt.grid()

    current_axes = plt.gca()
    current_axes.invert_yaxis()
    current_axes.axes.set_yticks(range(0, len(pixel_array)))
    current_axes.axes.set_xticks(range(0, len(pixel_array)))

    plt.tick_params(axis='both', left=False, top=False, right=False, bottom=False, labelleft=False, labeltop=False,
                    labelright=False, labelbottom=False)

    plt.figtext(0.5, 0.01, board_description, ha="center", fontsize=14)
    plt.show()


def create_random_binary_matrix(n):
    return np.random.randint(0, 2, size=(n, n))
