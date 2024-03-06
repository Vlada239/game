import unittest
from unittest import TestCase, main
from game import mas, check_win


# python -m unittest discover tests

class TestGridWinner(unittest.TestCase):

    def test_first_row_check_win(self):
        mas[0][0] = "x"
        mas[0][1] = "x"
        mas[0][2] = "x"
        self.assertTrue(check_win("x"))

    def test_second_row_is_winner(self):
        mas[1][0] = "x"
        mas[1][1] = "x"
        mas[1][2] = "x"
        self.assertTrue(check_win("x"))

    def test_third_row_is_winner(self):
        mas[2][0] = "x"
        mas[2][1] = "x"
        mas[2][2] = "x"
        self.assertTrue(check_win("x"))

    def test_first_column_is_winner(self):
        mas[0][0] = "x"
        mas[1][0] = "x"
        mas[2][0] = "x"
        self.assertTrue(check_win("x"))

    def test_second_column_is_winner(self):
        mas[0][1] = "x"
        mas[1][1] = "x"
        mas[2][1] = "x"
        self.assertTrue(check_win("x"))

    def test_third_column_is_winner(self):
        mas[0][2] = "x"
        mas[1][2] = "x"
        mas[2][2] = "x"
        self.assertTrue(check_win("x"))

    def test_first_diagonal_is_winner(self):
        mas[0][0] = "x"
        mas[1][1] = "x"
        mas[2][2] = "x"
        self.assertTrue(check_win("x"))

    def test_second_diagonal_is_winner(self):
        mas[0][2] = "x"
        mas[1][1] = "x"
        mas[2][0] = "x"
        self.assertTrue(check_win("x"))
