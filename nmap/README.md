# nmap 使い方チートシート

TCPスキャンとUDPスキャンをしてscan.txtに結果を保存する

```
$ sudo nmap -sC -sV -A -o scan.txt 10.10.10.209  
```

## 主なオプション  

### -sV
サービスのバージョンを表示  

### -sS  
TCP SYN スキャン  

### OS検出・バージョン検出・スクリプトスキャン・トレースルート   
```
nmap -A <IP Address>
```

## OS検出
```
nmap -O <IP Address>
```

### 高速スキャン
```
nmap -F <IP Address>
```

### -v
詳細情報を出力させる  

### -p [port no]
ポート番号の指定  
全ポートを選択する場合は、下記のようにする  
すっごい時間がかかるので注意  
```
nmap -p- <IP Address>
```

### IPアドレスの範囲指定
```
nmap 192.168.0.1-254  
```

### 送信元IPを偽装
nmap -e インタフェース名 -S 偽装したい送信元IP IPアドレス   

### 踏み台を使用
nmap -sI 踏み台サーバー IPアドレス  

### Pingを飛ばさない
```
nmap -P0 <IP Address>
```

### TCP SYN スキャン
```
nmap -sS <IP Address>
```

### 利用される可能性が高いポートに対してTCP SYNスキャン
nmap はデフォルトだと1000ポートまでしか調査しない。(昔は違った？)  
そのためnmap-services にあるポート対象にしたい場合には、「--port-ratio=0.0」 をつける必要がある。
```
sudo sudo nmap -v -sS --port-ratio=0.0 <IP Address>
```
参照：https://qiita.com/watarin/items/736b53b52675ef041e1c

### すべてのポートをスキャンし、見つかったポートのソフト種別やバージョンも調べる
```
sudo nmap -p 1-65535 -T4 -A -v <IP Address>
```