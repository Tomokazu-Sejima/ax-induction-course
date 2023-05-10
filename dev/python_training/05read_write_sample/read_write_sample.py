"""ファイルの読み書き
"""

import os


def create_write_file(filename, text):
    """ファイルを新規作成しテキストを書き込む

    Args:
        filename (string): ファイル名
        text (string): テキスト
    """

    # 引数に"x"を与えることで、ファイル新規作成+書き込み
    f = open(filename, "x")
    f.write(text)
    f.close()


def read_file(filepath):
    """ファイルを読み込む
    _type_: _description_
    """

    f = open(filepath, "r")

    # 開いたファイル全体を文字列として取得
    text = f.read()
    print(text)

    # 【課題】他にどのような読込用メソッドがあるか調べてみましょう。

    f.close()


if __name__ == "__main__":
    filename = "sample.txt"
    create_write_file(filename, "Hello, World!")

    filepath = "./" + filename
    read_file(filepath)

    os.remove(filepath)
