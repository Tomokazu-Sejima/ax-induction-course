"""分岐
"""

import sys


def max_int(a, b, c):
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
