""" クラス
"""


class Calc:
    """計算クラス"""

    # コンストラクタ
    # インスタンス生成時に実行される
    # "self"はインスタンス自身を表す。すべてのメソッドにselfが必要
    # ※なお、名前を"self"以外のキーワードにすることは可能ですが、慣例としてselfを使用しています。
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def plus(self):
        """足し算"""
        print(self.x + self.y)

    def minus(self):
        """引き算"""
        print(self.x - self.y)

    def times(self):
        """掛け算"""
        print(self.x * self.y)

    def divided(self):
        """割り算"""
        print(self.x / self.y)


# モジュールがPythonスクリプトとして起動された場合に実行する処理
if __name__ == "__main__":
    calculation = Calc(1, 2)
    calculation.plus()
    calculation.minus()
    calculation.times()
    calculation.divided()
