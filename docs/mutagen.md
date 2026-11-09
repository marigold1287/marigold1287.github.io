---
tags:
    - tech
---
# pythonのタグ編集パッケージ「mutagen」
長年溜め込んできた音楽ファイルのタグを整理する際に
[Picard](./picard.md)と合わせて使用した。

1つのファイルに複数の規格のタグが混在していると
再生ソフト側で意図しない情報が表示される場合があるため
余計なものはしておいたほうが良い。
## APEタグ
Monkey's Audioで使われているタグ。

タグの開始を示すヘッダーとタグの終わりを示すフッターの間に書き込まれる。

現在これが使われることが殆どない?だろうから、消しておくといい。

```python
from pathlib import Path
from mutagen.apev2 import APEv2, APENoHeaderError

file = Path("/path/to/file.mp3")

def delete_ape_tag(file: Path):
    try:
        ape = APEv2(file)

        ape.delete()
        ape.save()
    except APENoHeaderError:
        # print("No APE TAG")
        pass
```

## MP3タグ
ID3v1([mp3のタグ](./mp3-id3-tag.md)も参照)を削除する

```python
from pathlib import Path
from mutagen.id3 import ID3

file = Path("/path/to/file.mp3")

def delete_id3v1_tag(file: Path):
    audio = ID3(file)
    audio.save(v1=0)
```

## タグを見る
```python
print(audio.pprint())
```
で人間が読みやすい形でタグの内容を表示させることができる。
