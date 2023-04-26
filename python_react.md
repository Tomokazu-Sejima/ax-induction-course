# Python / React 研修

### 環境構築

#### Windows

- [WSL + ubuntu](https://learn.microsoft.com/ja-jp/windows/wsl/install)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Visual Studio Code](https://azure.microsoft.com/ja-jp/products/visual-studio-code)

#### WSL

- [fish](https://fishshell.com/)
- [asdf (Programming Language Manager)](https://asdf-vm.com/)
  - [python](https://github.com/asdf-community/asdf-python)
  - [nodejs](https://github.com/asdf-vm/asdf-nodejs)
- [PDM (Python package and dependency manager)](https://pdm.fming.dev/latest/)

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

### Gatsby (React based framework) でフロントエンドアプリを作成する

1. Gatsby CLI のインストール
   ```
   npm install -g gatsby-cli
   ```
2. [Create a Gatsby site](https://www.gatsbyjs.com/docs/tutorial/getting-started/part-1/#create-a-gatsby-site)

3. [Tutorial](https://www.gatsbyjs.com/docs/tutorial/getting-started/part-1/)の"Part 2: Use and Style React Components"まで進める

### フロントエンド(React)とバックエンド(django)の繋ぎ込み

#### django

1. `tutorial/settings.py`の`INSTALLED_APPS`, `MIDDLEWARE`を更新  
   (公式の[Setup](https://github.com/adamchainz/django-cors-headers#setup)を参考にしてください。)
2. `tutorial/settings.py`に`CORS_ALLOWED_ORIGINS`を作成
   ```
   CORS_ALLOWED_ORIGINS = [
       "http://localhost:3000",
       "http://127.0.0.1:3000",
   ]
   ```

#### React

### その他

#### なぜプロジェクト毎にパッケージ管理する必要があるのか

TBD

#### 便利ツール

- tree  
   カレントディレクトリの情報を tree 状に確認できます。

  ```
  # インストール
  sudo apt install tree
  ```

  ```
  .
  ├── manage.py
  ├── snippets
  │   ├── __init__.py
  │   ├── admin.py
  │   ├── apps.py
  │   ├── migrations
  │   │   └── __init__.py
  │   ├── models.py
  │   ├── tests.py
  │   └── views.py
  └── tutorial
      ├── __init__.py
      ├── __pycache__
      │   ├── __init__.cpython-310.pyc
      │   └── settings.cpython-310.pyc
      ├── asgi.py
      ├── settings.py
      ├── urls.py
      └── wsgi.py

  4 directories, 15 files
  ```
