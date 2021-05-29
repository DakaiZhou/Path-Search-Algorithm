import numpy as np


def board_creator(n, m):
    board = np.random.randint(m, size=(n, n))
    return board