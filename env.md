# 環境構築

Linux のプログラムを Windows 上で実行するためのツール [WSL](https://learn.microsoft.com/ja-jp/windows/wsl/about) を使用します。

### Windows

- [WSL + ubuntu](https://learn.microsoft.com/ja-jp/windows/wsl/install)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Visual Studio Code](https://azure.microsoft.com/ja-jp/products/visual-studio-code)
- [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=ja-jp&gl=jp)

### WSL

- [fish (command line shell)](https://fishshell.com/)
- [asdf (Programming Language Manager)](https://asdf-vm.com/)
  - [python](https://github.com/asdf-community/asdf-python)
  - [nodejs](https://github.com/asdf-vm/asdf-nodejs)
- [PDM (Python package and dependency manager)](https://pdm.fming.dev/latest/)

#### Tips

- fish

  - Go fish > Linux > Subscribe > `To install fish, run the following commands:`  
    のコマンドを実行

  - デフォルトの shell を fish に変更  
    実行後は要再起動
    ```
    chsh -s $(which fish)
    ```

- Python のインストール (asdf)

  - Python のインストールに失敗する場合は必要なパッケージを Ubuntu にインストールする

    ```
    sudo apt-get update && sudo apt-get install make build-essential libssl-dev \
    zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev \
    liblzma-dev
    ```

- PDM のインストール

  - [pipx](https://pypa.github.io/pipx/)を使用したインストール推奨
  - PDM コマンドがエラーになる場合は、`.config/fish/config.fish`に  
    `export PATH="$PATH:/home/<ユーザ名>/.local/bin"`を追加

- コマンドの実行時にエラーが発生する場合、
  - `source ~/.config/fish/config.fish` を実行  
    fish shell の設定ファイルを再読み込みします。
  - `.config/fish/config.fish` に `export PATH="$PATH:/home/<ユーザ名>/.local/bin"`を追加
