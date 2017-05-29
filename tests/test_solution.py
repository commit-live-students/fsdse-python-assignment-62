from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        from random import randint

        num1 = randint(100, 1000)
        num2 = randint(100, 1000)
        num3 = randint(100, 1000)
        num4 = randint(100, 1000)

        l = [num1, num2, num3, num4]

        self.assertTrue(solution(l)[0], num1)
        self.assertTrue(solution(l)[0], num2)
        self.assertTrue(solution(l)[0], num3)
        self.assertTrue(solution(l)[0], num4)