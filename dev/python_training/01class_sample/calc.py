""" クラス
"""


class Calc:
    """計算クラス"""

    # コンストラクタ
    # インスタンス生成時に実行される
    # "self"はインスタンス自身を表す。すべてのメソッドにselfが必要
    # ※なお、名前を"self"以外のキーワードにすることは可能ですが、慣例としてselfを使用しています。
    def __init__(self, x: int, y: int):
        # インスタンス変数を定義
        self.x = x
        self.y = y

    def plus(self):
        """足し算"""
        return self.x + self.y

    def minus(self):
        """引き算"""
        return self.x - self.y

    def times(self):
        """掛け算"""
        return self.x * self.y

    def divided(self):
        """割り算"""
        return self.x / self.y


# モジュールがPythonスクリプトとして起動された場合に実行する処理
if __name__ == "__main__":
    # インスタンス生成
    calculation = Calc(1, 2)
    print(calculation.plus())
    print(calculation.minus())
    print(calculation.times())
    print(calculation.divided())
