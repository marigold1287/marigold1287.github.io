---
tags:
    - tech
---
# YAMLとTOMLの書き方
YAML Ain't Markup Language、Tom's Obvious, Minimal Languageの略で
どちらも設定ファイルを記述するときによく使われる。

## 記法
### YAML
YAMLでは key: value が辞書、- がリストの要素を表す。リストの要素には値・辞書・さらにリストを書くことができる。

### TOML
テーブルが辞書のキーを表す。テーブル配列`[[]]`は辞書の配列を作るときに用いる。

## リスト
=== "JSON"
    ```json
    "tags": [
        "a",
        "64",
        "c"
    ]
    ```

=== "yaml"
    ```yaml
    tags:
        - a
        - "64"
        - "c"
    ```
=== "toml"
    ```toml
    tags = ["a", "64", "c"]
    ```

## 複数要素を持つ辞書
=== "JSON"
    ```json
    "date": {
        "created": "2025-12-31",
        "updated": "2026-01-02"
    }
    ```

=== "yaml"
    ```yaml
    date:
        created: 2025-12-31
        updated: 2026-01-02
    ```

=== "toml"
    ```toml
    [date]
        "created" = "2025-12-31"
        "updated" = "2026-01-02"
    ```


## 辞書
=== "JSON"
    ```json
    "category": "Hoge",
    ```

=== "yaml"
    ```yaml
    category: hoge
    ```
=== "toml"
    ```toml
    category = "hoge"
    ```

## 辞書のリスト
=== "JSON"
    ```json
    "relations": [
        {
            "type": "FOO",
            "target": "hoge",
            "at": "2026-12-15"
        },
        {
            "type": "HAS_ALIAS",
            "target": "hoge"
        }
    ]
    ```

=== "yaml"
    ```yaml
    relations:
        - type: FOO
          target: hoge
          at: 2026-12-15
        - type: HAS_ALIAS
          target: hoge
    ```
=== "toml"
    ```toml
    [[relations]]
        type = "FOO"
        target = "hoge"
        at = "2026-12-15"
    [[relations]]
        type = "HAS_ALIAS"
        target = "hoge"
    ```

## Pythonで読み取る
### パッケージをインストール
```bash
pip install pyyaml
pip install toml
```

### YAML
```python
import yaml

with open("./test.yml", "r") as f:
    document = yaml.safe_load(f)

    print(json.dumps(document, indent=4, default=str))
```

### TOML
```python
import toml

with open("./test.toml", "r") as f:
    document = toml.load(f)

    print(json.dumps(document, indent=4, default=str))
```

## フロントマター
YAMLは `---`, TOMLは`+++`を使う。
