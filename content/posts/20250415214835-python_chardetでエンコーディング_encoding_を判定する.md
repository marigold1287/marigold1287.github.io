+++
title = "python chardetでエンコーディング(encoding)を判定する"
author = ["K"]
date = 2025-04-15T22:14:02+09:00
lastmod = 2025-04-15T22:16:55+09:00
tags = ["python"]
categories = ["tech"]
draft = false
showtoc = true
+++

## 課題 {#課題}

```python
with open("textfile.txt", "r", encoding="sjis") as f:
    tmp = f.read()
```

`UnicodeEncodeError: 'shift_jis' codec can't encode character '\uff5e' in position 4807: illegal multibyte sequence`
というエラーが出て読み込みに失敗する場合がある。


## 原因 {#原因}

`encoding` の指定が適切でない。


## 解決 chardetでエンコーディングを判定する {#解決-chardetでエンコーディングを判定する}

pythonの `chardet` というパッケージを使うとバイト列から文字コードを推定することができる。

まずはインストール。

```bash
python -m pip install chardet
```

とりあえずバイトデータのまま読み込んで `chardet` で解析。

```python
with open("textfile.txt", "rb") as f:
    bytestring = f.read()  # バイト文字列

result = chardet.detect(bytestring)
```

resultは `{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}` で99%の確率で `utf-8` ということがわかる。

そうしたらバイト列をデコードする

```python
string = bytestring.decode(result["encoding"])
```

これで元の文字列を得ることができる。


## 文字コード {#文字コード}

この問題はoutlookの `.msg` ファイルを `extract-msg` で解析しようとしていたときに直面したのだが、
`sjis` ではうまく行かなくて `cp932` ([Microsoftコードページ932 - Wikipedia](https://ja.wikipedia.org/wiki/Microsoft%E3%82%B3%E3%83%BC%E3%83%89%E3%83%9A%E3%83%BC%E3%82%B8932))でうまく行くという場合も多かった。

中国語だと `GB2312` と表示される場合が多いが、 `GBK` とか `GB18030` も試すと良い。ドイツ語だと `ISO 8859-1` 。


## 用語 {#用語}

あっているか分からないけど


### 文字コード {#文字コード}

1文字1文字に識別番号を与えて区別したもの。 `shift-jis` とか `utf-8` とか。


### エンコーディング {#エンコーディング}

文字列を文字コードに従ってバイト列へ変換すること


### デコーディング {#デコーディング}

バイト列をもとの文字列に変換すること
