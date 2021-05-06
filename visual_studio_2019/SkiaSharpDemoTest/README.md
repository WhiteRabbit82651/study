# Skia Sharpのデモを実行してみた(VisualStudio2019ならできる)

## ローカルファイルを表示する

- 画像ファイルをフォルダごと取り込む  
![](./img/1.png)

- csproj ファイルにItemGroupとしてリソースIDを追加する  
- <font color="#FF0000">VisualStudio2017ではcsprojファイルが存在しないため、リソースIDの記述する箇所がわからない</font>  
![](./img/2.png)

- Assembly で リソースIDのファイルを読み込み、SKBitmapにDecodeする  
- <font color="#FF0000">VisualStudio2017ではリソースIDの記述方法がわからず、Assemblyで取得できないので、streamがNULLになる</font>  
![](./img/3.png)

- SKBitmapが作成できていたら、DrawBitmapで画面に表示する  
- <font color="#FF0000">VisualStudio2017ではstreamがNULLなので、画像が表示されない</font>  
![](./img/4.png)

## ネットから取得する

- urlを指定してHttpClientを使ってStreamを開き、MemoryStreamに取得する  
- 取得したMemoryStreamをSKBitmapにDecodeする  
- <font color="#FF0000">VisualStudio2017ではHttpClientが読み込めない。ネットが重いせいか、古いせいかは不明</font>  
- <font color="#FF0000">HttpClientが読み込めないのでstreamが開けずこちらも画像が読み込めない</font> 
![](./img/5.png)

- DecodeしたSKBitmapをDrawBitmapで表示する  
![](./img/6.png)

## 結果
![](./img/7.png)

## バージョン問題
- そもそもバージョンが違うのだから、コンパイル後の速度も違うのでは？  
![](./img/8.png)

