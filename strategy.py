import numpy as np
import create_game as cg


def get_neighbors(row, col, num_row, num_col):
    """
    get the neighbors of the element
    :param row: row index
    :param col: column index
    :param num_row: number of rows
    :param num_col: number of columns
    :return: index of four neighbors
    """
    if row == 0:
        up = None
    else:
        up = [row-1, col]
    if col == 0:
        left = None
    else:
        left = [row, col - 1]
    if col == num_col - 1:
        right = None
    else:
        right = [row, col + 1]
    if row == num_row - 1:
        down = None
    else:
        down = [row + 1, col]
    return [up, down, left, right]


def visit_process(comp, vis_mat, board, row, col, num_row, num_col):
    """
    mark a matrix with 1 if the element is visited, to avoid repeated visit, return the updated component
    :param comp: connected component
    :param vis_mat: visit matrix, 1, 0
    :param board: the game status
    :param row: row index
    :param col: column index
    :param num_row: number of rows of the game
    :param num_col: number of columns of the game
    :return: updated connected component which connects to the origin
    """
    neighbors = get_neighbors(row, col, num_row, num_col)
    for nei in neighbors:
        if nei is not None:
            if vis_mat[nei[0], nei[1]] != 1:
                vis_mat[nei[0], nei[1]] = 1
                if board[nei[0], nei[1]] == board[0, 0]:
                    comp[nei[0], nei[1]] = 1
                    comp = visit_process(comp, vis_mat, board, nei[0], nei[1], num_row, num_col)
    return comp


def find_connected_component(board):
    """
    to find the connected component which connects to the origin
    :param board: the current game board
    :return: final connected component which connects to the origin
    """
    shape = np.shape(board)
    visit = np.zeros(shape)
    comp = np.zeros(shape, dtype=int)  # added avoid for data type conflict
    comp[0, 0] = 1

    target = board[0][0]
    for i in range(shape[0]):  # added stop condition for row update
        if board[i, 0] != target:
            break
        for j in range(shape[1]):
            if board[i][j] != target:
                break
            else:
                visit_process(comp, visit, board, i, j, shape[0] , shape[1] )
    return comp


def find_boundary(comp):
    """
    find the boundary of the connected component
    :param comp: component
    :return: the boundary
    """
    shape = np.shape(comp)
    boundary = []
    for i in range(shape[0]):
        for j in range(shape[1]):
            if comp[i, j] == 0:
                neighbors = get_neighbors(i, j, shape[0], shape[1])
                for nei in neighbors:
                    if nei is not None:
                        if comp[nei[0], nei[1]] == 1:
                            boundary.append([i, j])
                            break  # indented one more, it needs to break the most inner for loop
    return boundary


def choose_color(board, boundary):  # idx iss not needed deleted
    """
    choose the color
    :param board: current game board
    :param boundary: the boundary that used to decide which color to choose
    :return: the color and the
    """
    color = []
    print("Boundary: {}".format(boundary))
    for b in boundary:
        color.append(int(board[b[0], b[1]]))
    color = np.array(color)
    print("color: {}".format(color))
    counts = np.bincount(color)
    choose = np.argmax(counts)
    return choose


def update_board(board, comp, color):
    """

    :param board: current game board
    :param comp: connected component
    :param color: the color need to change to
    :return: updated game board
    """
    # do not need
    # for i in idx:
    #     board[i[0], i[1]] = color
    board[comp == 1] = color
    return board


if __name__ == '__main__':
    game_board = cg.board_creator(6, 4)
    print(game_board)
    while not ((game_board == game_board[0, 0]).all()):
        component = find_connected_component(game_board)
        print("Component: ")
        print(component)
        bry = find_boundary(component)
        c = choose_color(game_board, bry)
        game_board = update_board(game_board, component, c)
        print("/*******************/")
        print(game_board)







