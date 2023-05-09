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
    ans1 = get_sum([1, 2, 3])
    print(ans1)
    ans2 = factorial(5)
    print(ans2)
