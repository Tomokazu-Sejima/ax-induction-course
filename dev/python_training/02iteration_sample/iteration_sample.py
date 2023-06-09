"""ループ
"""


def repeat_output(name: str, count: int):
    """指定された回数分 "XXさん、こんにちは" と出力します。

    Args:
        name (str): Your Name
        count (int): 繰り返し回数
    """

    for n in range(count):
        print(f"{name}さん、こんにちは。")

    ## C#の例
    # for (int n = 0; n < count; n ++){
    #   Console.WriteLine("{0}さん、こんにちは。", name)
    # }


# 関数の定義
# def 関数名(引数):
# 引数に型はあってもなくてもいい
def get_sum(numbers):
    """配列の要素の合計値を求める

    Args:
        numbers (list): int型の配列

    Returns:
        int: 配列の要素の合計値
    """

    ans = 0
    for number in numbers:
        ans += number

    return ans


def factorial(number):
    """階乗を求める

    Args:
        number (int): 任意の自然数n

    Returns:
        int: 1からnまでのすべての自然数の積
    """

    ans = 1
    for n in range(1, number + 1):
        ans *= n

    return ans


if __name__ == "__main__":
    repeat_output("太郎", 10)
    ans1 = get_sum([1, 2, 3])
    print(ans1)
    ans2 = factorial(5)
    print(ans2)
