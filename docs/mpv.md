---
tags:
    - tech
---
# コンソール上で動作する軽量プレイヤー mpv
[mpg123](./mpg123.md)よりも多機能。aac等も再生できる。

## シャッフル再生
```bash
find ~/Music -type f -iname '*.mp3' | mpv --no-video --af=dynaudnorm --shuffle --playlist=-
```
- `-`は標準出力のこと。見つかったファイルをプレイリストに追加する
- `--no-video`はアートワーク等を表示させないためのオプション
- `--af=dynaudnorm`は音量ノーマライズ

findをうまいこと使って聴きたい曲を抽出する...

## ストリーミング
```bash
mpv  https://somafm.com/groovesalad130.pls
```
## マニュアル
<https://mpv.io/manual/stable/>
