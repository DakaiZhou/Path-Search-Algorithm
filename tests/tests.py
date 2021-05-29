import unittest
import numpy as np
import create_game as cg
import strategy as st


class TestGameCreator(unittest.TestCase):

    def test_board_creator(self):
        board = cg.board_creator(3, 3)
        self.assertTrue((np.shape(board)[0] == np.array([3, 3])).all())
        self.assertTrue((board < 3).all())
        self.assertNotEqual(np.max(board), np.min(board))


class TestStrategy(unittest.TestCase):
    def test_find_connected_component(self):
        a = np.array([[1, 0, 1], [1, 1, 1], [0, 0, 0]])
        a2 = np.array([[1, 0, 1], [1, 1, 1], [0, 2, 0]])
        res = st.find_connected_component(a2)
        b = st.find_boundary(res)
        c = st.choose_color(a2, b)
        updated = st.update_board(a2, res, c[0], c[1])
        neighbor1 = st.get_neighbors(0, 0, 3, 3)
        neighbor2 = st.get_neighbors(0, 2, 3, 3)
        neighbor3 = st.get_neighbors(2, 0, 3, 3)
        neighbor4 = st.get_neighbors(2, 2, 3, 3)
        neighbor5 = st.get_neighbors(1, 1, 3, 3)

        self.assertTrue((a == res).all())
        self.assertEqual(b, [[0, 1], [2, 0], [2, 1], [2, 2]])
        self.assertEqual(c[0], 0)
        self.assertEqual(c[1], [[0, 1], [2, 0], [2, 2]])
        self.assertEqual(neighbor1, [None, [1, 0], None, [0, 1]])
        self.assertEqual(neighbor2, [None, [1, 2], [0, 1], None])
        self.assertEqual(neighbor3, [[1, 0], None, None, [2, 1]])
        self.assertEqual(neighbor4, [[1, 2], None, [2, 1], None])
        self.assertEqual(neighbor5, [[0, 1], [2, 1], [1, 0], [1, 2]])
        self.assertTrue(([[0, 0, 0], [0, 0, 0], [0, 2, 0]] == updated).all())