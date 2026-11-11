---
tags:
    - tech
date: 2026-11-10
---
# リプレイゲイン設定ツール rsgain
<https://github.com/complexlogic/rsgain>

```bash
sudo apt install rsgain
```

詳しい設定はあまり調べていないが

```bash
rsgain easy .
```

とするととりあえずいい感じになる。
ただ、`easy`の場合はアルバムごとにフォルダ分けされている前提で処理されるらしく、
そうでないなら別途設定が必要になるかもしれない。

[Picard](./picard.md)とも連携していて、Picard側でリプレイゲインの設定を有効にして
rsgainの実行ファイルのパスを登録しておくとアルバムごとに解析することができる。

## 関連
- [リプレイゲイン](./replaygain.md)
