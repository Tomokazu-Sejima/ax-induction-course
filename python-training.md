# Python 研修

### WSL (Ubuntu) 上で Python プログラムを実行する

1. ディレクトリを作成して、作成したディレクトリに移動
   ```bash
   mkdir dev && cd dev
   ```
2. ソースファイル作成
   ```bash
   touch hello.py
   ```
3. Visual Studio Code で開く
   ```bash
   code hello.py
   ```
4. `hello.py` ファイルにコードを書く
   ```python
   print("Hello, World!")
   ```
5. 実行
   ```bash
   python hello.py
   ```

### Python で API サーバーを構築する

ここでは、[django REST framework](https://www.django-rest-framework.org/) を用いて、API サーバーを構築します。

1. dev ディレクトリに移動
   ```bash
    cd dev
   ```
2. Create django App
   ```bash
   pip install django
   django-admin startproject tutorial
   cd tutorial
   python manage.py startapp snippets
   ```
3. Python プロジェクト管理の初期化  
    ※質問は全て Enter で OK
   ```bash
   pdm init
   ```
4. Python パッケージのインストール
   ```bash
   pdm add django
   pdm add djangorestframework
   pdm add django-cors-headers
   ```
5. PDM Script の作成  
   `pyproject.toml`に下記を追加

   ```bash
   [tool.pdm.scripts]
   server = "python manage.py runserver"
   makemigrations = "python manage.py makemigrations"
   migrate = "python manage.py migrate"
   ```

6. 実行
   ```bash
   pdm run migrate
   pdm run server
   ```
7. [Tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/)の"Tutorial 2: Requests and Responses"まで進める
