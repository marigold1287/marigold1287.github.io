+++
title = "datatablesのselect API"
author = ["K"]
date = 2025-03-10T00:14:53+09:00
lastmod = 2025-03-30T14:43:44+09:00
tags = ["datatables", "javascript"]
categories = ["tech"]
draft = false
showtoc = true
+++

[Download](https://datatables.net/download/index)時にSELECTも含めておく。

初期化時に

```javascript
$("#table").DataTable({
    select: true
})
```

これは1つだけ選択する場合。 `multi` にすると複数選択できるようになる。


## serverSideを使用しているときはrowIdも設定する {#serversideを使用しているときはrowidも設定する}

データをサーバーから取ってくるようにしている場合は主キーに該当する列をrowIdに設定する必要がある。

```javascript
$("#table").DataTable({
    select: true,
    rowId: function(row) {
        return row["key"];
    }
})
```

これがないとリロード時にselectがリセットされてしまう。
(<https://datatables.net/extensions/select/examples/initialisation/server-side-processing.html>)


## 選択されたすべてのデータを取得する cumulative {#選択されたすべてのデータを取得する-cumulative}

```javascript
selectedIds = $("#table_id").DataTable().select.cumulative();
```

`rowId` のリストを取得できる


## event {#event}

[イベント]({{< relref "20250307162536-datatablesのイベント処理.md" >}})も使用可能で、

```javascript
// アイテムが選択された時
    table.on('select', function (e, dt, type, indexes) {
        console.log('Items to be selected are now: ', type, indexes);
        if (type == "row") {
            var data = dt.rows(indexes).data().toArray();
            console.log(data)
        }
    });

// アイテムが選択解除された時
table.on('deselect', function (e, dt, type, indexes) {
    console.log('Items to be deselected are now: ', indexes);
});
```

(<https://datatables.net/reference/event/select>)


## 読み込み時に特定のデータにチェックを入れる {#読み込み時に特定のデータにチェックを入れる}

特にサーバーサイドで実行している場合に有用。

サーバーサイド処理を有効にしている時、セレクトされたデータのリストは

```js
$("#table_id").DataTable().context[0]._select_set
```

にリストとして保存されている。

チェックしたいデータの配列を代入してTableをDrawし直すとチェックされた状態のテーブルを描画することができる。

```js
selected_ids = [1, 2, 3, 5];
if (selected_ids) {
    api.context[0]._select_set = selected_ids;
    api.draw();
}
```


## columnにチェックボックスを表示する {#columnにチェックボックスを表示する}

```js
columns: [
    {
        "data": null,
        "name": "is_selected",
        "render": DataTable.render.select(),
        "orderable": false,
        "searchable": false
    },
    // ...
]
```

select optionは次のように設定する。

```js
select: {
    style: 'multi',
    selector: 'td:first-child',
    headerCheckbox: 'select-page'
},
```

`orderable` を有効にする場合はサーバーに選択されたIDのリストを送って別途処理プログラムを実装する必要がある。

pandasのDataFrameでデータを処理しているなら

```python
def add_is_selected_column_to_dataframe(self, df, selected_ids):
    if not selected_ids:  # 空リストなら即 False
        df["is_selected"] = False
        return df

    masks = []
    for selected_id in selected_ids:
        # rowIdはjson文字列 {"id_a": 2, "id_b": 3}になっている
        ids = json.loads(selected_id)
        if not ids:
            continue

        mask = pd.DataFrame({
            key: df[key] == value for key, value in ids.items()
        }).all(axis=1)
        masks.append(mask)

    # `masks` が空なら、全 False の Series を作る
    if masks:
        df["is_selected"] = pd.concat(masks, axis=1).any(axis=1)
    else:
        df["is_selected"] = False

    return df
```

これでセレクトされたレコードがTrue、そうでない場合がFalseの列を追加することができる。
