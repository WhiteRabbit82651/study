
# git command cheat sheet

## 既存のプロジェクトをgithubに追加する方法
```
echo "# CSharpWifiSetting" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin githubのURL(https://github.com/ユーザー名/プロジェクト名.git)
git push -u origin master
```
## push時にユーザー名とパスワードを省略する方法】
{cloneしたリポジトリDir}/.git/configを編集する  
```
[remote "origin"]
	url = https://username:password@github.com/username/repository.git
```

## 基本コマンド

### リモートリポジトリをローカルにクローンする
```
git clean [repository]
```

### フェッチする
フェッチとは、取りに行く、取ってくる、持ってくる、連れてくる、来させる、呼び出す、引き出す、惹きつける、などの意味を持つ英単語。  
gitの場合リモートから最新情報をローカルに持ってくる。  
場所は「master」ブランチではなく、「origin/master」ブランチに取り込まれる。
```
git fetch --all -p
```

### プルする
プルとは、引く（こと）、引っ張る、引き寄せる、引手、などの意味を持つ英単語。  
gitの場合、他のリポジトリ（リモート・リポジトリなど）のデータを取得し、ローカルのブランチに統合する。
```
git pull --ff
```

### 修正したファイルをローカルに反映させる
```
git add [file name]
```

### 修正をすべてローカルに反映させる
意図していないファイルまで反映されることもあるので、注意。
```
git add -u
```

### 修正をなかったことにする
```
git checkout [file name]
```

### ローカルのoriginブランチに修正を反映させる
git addしたファイルの修正を反映させる。  
```
git commit -m "comment"
```

### ローカルのoriginブランチに修正を反映させる
こちらはコメント用にエディタを開いて反映させる。  
起動するエディタは.git/configに記述されている。  
```
git commit -v
```

### リモートのoriginブランチに修正を反映させる
```
git push origin main
```

### ブランチを変更する
```
git checkout [branch name]
```

### カレントブランチを元に新にブランチを作成する
```
git checkout -b [new branch name]
```

### ブランチ一覧を表示する
```
git branch
```
