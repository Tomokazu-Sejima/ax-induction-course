# Web アプリケーション研修

### フロントエンド(React)とバックエンド(django)の繋ぎ込み

#### django

1. `tutorial/settings.py`の`INSTALLED_APPS`, `MIDDLEWARE`を更新  
   (公式の[Setup](https://github.com/adamchainz/django-cors-headers#setup)を参考にしてください。)
2. `tutorial/settings.py`に`CORS_ALLOWED_ORIGINS`を作成
   ```
   CORS_ALLOWED_ORIGINS = [
       "http://localhost:8000",
       "http://127.0.0.1:8000",
   ]
   ```
3. **今後は`pdm run server 8080`で実行してください**

#### React
