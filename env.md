# 環境構築

### Windows

- [WSL + ubuntu](https://learn.microsoft.com/ja-jp/windows/wsl/install)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Visual Studio Code](https://azure.microsoft.com/ja-jp/products/visual-studio-code)

### WSL

- [fish](https://fishshell.com/)
- [asdf (Programming Language Manager)](https://asdf-vm.com/)
  - [python](https://github.com/asdf-community/asdf-python)
  - [nodejs](https://github.com/asdf-vm/asdf-nodejs)
- [PDM (Python package and dependency manager)](https://pdm.fming.dev/latest/)

#### Tips

- Python のインストール (asdf)

  - 必要なパッケージを Ubuntu にインストールする

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
