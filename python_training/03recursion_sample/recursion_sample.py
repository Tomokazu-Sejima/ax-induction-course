import sys


def factorial(n):
    """階乗を求める

    Args:
        n (int): 階乗を求めたい数

    Returns:
        int: 1からnまでのすべての自然数の積
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    # コマンドライン引数を受け取る
    n = int(sys.argv[1])
    print(factorial(n))
