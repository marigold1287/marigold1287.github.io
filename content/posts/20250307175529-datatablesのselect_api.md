+++
title = "datatablesのselect API"
author = ["K"]
date = 2025-03-10T00:14:53+09:00
lastmod = 2025-03-10T00:15:12+09:00
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
var data = dt.rows(selectedData.rows).data().toArray();
console.log(data)
```


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
