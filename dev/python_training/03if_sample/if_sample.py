"""分岐
"""

import sys


def max_int(a: int, b: int, c: int):
    """3つの整数のうち、最大のものを返します。

    Args:
        a (int): 任意の整数 a
        b (int): 任意の整数 b
        c (int): 任意の整数 c

    Returns:
        _type_: _description_
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


if __name__ == "__main__":
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    n3 = int(sys.argv[3])
    print(max_int(n1, n2, n3))
