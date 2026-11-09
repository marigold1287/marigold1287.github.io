---
tags:
    - tech
---
# FFmpeg
サンプルコード
## flacを192kbpsのmp3
```bash
ffmpeg -i song.flac -codec:a libmp3lame -b:a 192k song_192.mp3
```



## リンク
- <https://www.ffmpeg.org/>
