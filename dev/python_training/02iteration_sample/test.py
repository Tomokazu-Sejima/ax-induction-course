"""テスト
    事前準備: pip install pytest
    実行方法: pytest <test filename> (ここでは、pytest test.py)
"""
import iteration_sample


def test_get_sum():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 配列の要素の合計値を求める
    result = iteration_sample.get_sum(numbers)
    # assert という文の後ろにテストしたい式を記述
    assert result is 55


def test_factorial():
    number = 4
    result = iteration_sample.factorial(number)
    assert result is 24
