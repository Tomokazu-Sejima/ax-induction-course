# Python 研修

### Python で API サーバーを構築する

ここでは、[django REST framework](https://www.django-rest-framework.org/) を用いて、API サーバーを構築します。

1. プロジェクト用ディレクトリ作成
   ```
   mkdir dev && cd dev
   ```
2. Create django App
   ```
   pip install django
   django-admin startproject tutorial
   cd tutorial
   python manage.py startapp snippets
   ```
3. Python プロジェクト管理の初期化  
    ※質問は全て Enter で OK
   ```
   pdm init
   ```
4. Python パッケージのインストール
   ```
   pdm add django
   pdm add djangorestframework
   pdm add django-cors-headers
   ```
5. PDM Script の作成  
   `pyproject.toml`に下記を追加

   ```
   [tool.pdm.scripts]
   server = "python manage.py runserver"
   makemigrations = "python manage.py makemigrations"
   migrate = "python manage.py migrate"
   ```

6. 実行
   ```
   pdm run migrate
   pdm run server
   ```
7. [Tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/)の"Tutorial 2: Requests and Responses"まで進める
