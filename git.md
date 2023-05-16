# Git 研修

### Git とは

ファイルのバージョン管理が簡単にできるツール

- 古いバージョンに簡単に戻せる
- 新旧のファイルを一元管理できる
- 編集した履歴を複数人で共有できる
- 複数人で修正した部分を一つに統合できる

> https://backlog.com/ja/git-tutorial/

### Git コマンド (基礎)

- `git clone <url>` : 既存のリポジトリをローカル環境に複製
- `git switch <branch name>` : ブランチの切り替え
- `git switch -c <branch name>` : ブランチの作成
- `git add <file path>` : ローカルの変更をステージング (コミット対象のファイルを指定)
  - (例) `git add .` : 全てステージング
- `git commit -m "<commit message>"` : コミット
- `git push` : コミットをローカルリポジトリからリモートリポジトリに送る
- `git push --set-upstream origin <branch name>` : 上流ブランチを指定してプッシュ (リモートにブランチを発行する際に使用)
  - `git push -u origin <branch name>` : 省略形
- `git pull` : git リポジトリにある最新のソースコードを取得
- `git merge <branch name>` : 現在使用しているブランチに特定のブランチを取り込む
  - (例) `git merge remotes/origin/dev` : リモートの dev ブランチをマージ
- [よく使う Git コマンド 19 選！使い方を初心者向けにわかりやすく解説](https://www.sejuku.net/blog/5816)

### 認証簡素化

```bash
git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/libexec/git-core/git-credential-wincred.exe"
```

- 上記で失敗する場合 `Files/Git/mingw64/libexec/git-core/git-credential-manager.exe"`が存在する場合は、下記を試してください。
  ```
  git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/libexec/git-core/git-credential-manager.exe"
  ```
