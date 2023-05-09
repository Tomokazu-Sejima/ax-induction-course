import unittest
import iteration_sample


class IterationSampleTest(unittest.TestCase):
    def test_get_sum(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # 配列の要素の合計値を求める
        result = iteration_sample.get_sum(numbers)
        # assertEqualは期待値とメソッドの戻り値が等しいかチェックするメソッド
        self.assertEqual(55, result)

    def test_factorial(self):
        number = 4
        result = iteration_sample.factorial(number)
        self.assertEqual(24, result)


if __name__ == "__main__":
    unittest.main()
