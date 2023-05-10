"""例外処理
"""

import sys


class EmptyFileException(Exception):
    pass


def read_file(filepath):
    """ファイルを読み込む
    _type_: _description_
    """

    try:
        f = open(filepath, "r")
        # 開いたファイル全体を文字列として取得
        text = f.read()

        # ファイルの中身が空の場合、例外を発生させる
        if not text:
            raise EmptyFileException()

        print(text)

    # 例外のキャッチ
    # 上から順に評価される
    except FileNotFoundError:
        print("ファイルが存在しません")
    except EmptyFileException:
        print("ファイルの中身が存在しません")
        f.close()
    else:
        print("ファイルの読込に成功しました")
        f.close()
    finally:
        print("処理終了")


if __name__ == "__main__":
    filename = sys.argv[1]
    filepath = "./" + filename
    read_file(filepath)
