import unittest
import even_odd
import divisible
import triangles
import grades
import rock_paper_scissors
import assignment_four


class MyTestCase(unittest.TestCase):

    def test_is_divisible(self):
        self.assertTrue(divisible.is_divisible(30, 15))
        self.assertFalse(divisible.is_divisible(4, 9))

    def test_is_triangle(self):
        self.assertTrue(triangles.is_triangle(7, 11, 16))
        self.assertFalse(triangles.is_triangle(20, 7, 11))
        self.assertFalse(triangles.is_triangle(4, 9, 3))
        self.assertFalse(triangles.is_triangle(9, 13, 22))

    def test_points_1(self):
        self.assertEqual(2, grades.points(80, False))

    def test_points_2(self):
        self.assertEqual(0.2, grades.points(64, True))

    def test_points_3(self):
        self.assertEqual(3, grades.points(88, False))

    def test_rps(self):
        self.assertEqual("You win!", rock_paper_scissors.who_wins(3, 2))
        self.assertEqual("It is a tie", rock_paper_scissors.who_wins(1, 1))

    def test_get_card(self):
        card = assignment_four.get_card()
        self.assertGreaterEqual(card, 1)
        self.assertLessEqual(card, 10)

    def test_get_winner(self):
        self.assertEqual("the dealers total is 10 You Won!", assignment_four.get_winner(12, 10))
        self.assertEqual("the dealers total is 12 the dealer won", assignment_four.get_winner(10, 12))
        self.assertEqual("it was a tie", assignment_four.get_winner(10, 10))
        self.assertEqual("the dealers total is 10 You Won!", assignment_four.get_winner(21, 10))
        self.assertEqual("You went over 21. You lose", assignment_four.get_winner(22, 10))
if __name__ == '__main__':
    unittest.main()
