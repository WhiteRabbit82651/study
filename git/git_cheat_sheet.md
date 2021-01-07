------------------------------------
【push時にユーザー名とパスワードを省略する方法】
{cloneしたリポジトリDir}/.git/configを編集する
[remote "origin"]
	url = https://username:password@github.com/username/repository.git
------------------------------------
【基本コマンド】
git clean [repository]
git fetch --all -p
git pull --ff
git add [file name]
git add -u
git commit -m "comment"
git commit -v
git push origin main
