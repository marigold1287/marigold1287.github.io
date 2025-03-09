+++
title = "datatablesのcolumnsオプション"
author = ["K"]
date = 2025-03-10T00:12:14+09:00
lastmod = 2025-03-10T00:25:50+09:00
tags = ["datatables", "javascript"]
categories = ["tech"]
draft = false
showtoc = true
+++

## 例 {#例}

```js
const table = $("#tableId").DataTable({
    columns: [
        {
            name: "link",
            data: "data_id",
            orderable: false,
            render: function(data, type, row, meta) {
                return '<a href="/{{request.blueprint}}/' + data + '/edit">Edit</a>';
            }
        },
        { name: "name", data: "name", title: "Name",  },
        { name: "position", data: "position", title: "Position",  },
        { name: "salary", data: "salary", title: "Salary", },
        { name: "start_date", data: "start_date", title: "Start date",  },
        { name: "office", data: "office", title: "Office",  },
        { name: "extn", data: "extn", title: "Extn",  },
    ],
})

```


## name {#name}

列の名前。普通は

```js
table.columns(index).data().toArray();
```

みたいに番号で指定するが、 `name` を決めておくと

```js
table.columns("salary:name").data().toArray();
```

のように名前で列を指定できるようになる。


## data {#data}

DataTablesではデータをオブジェクトの形で

```js
data = [
    {
        "data_id": 1,
        "name": "Tiger Nixon",
        "position": "System Architect",
        "salary": "$320,800",
        "start_date": "2011/04/25",
        "office": "Edinburgh",
        "extn": "5421"
    },
]
```

のように渡すが、キー名を `data` の値として入力する。


## title {#title}

テーブルのヘッダーに表示される文字列。


## orderable {#orderable}

defaultは `true` 。列見出しの横に昇順or降順を示す矢印が出てきて、並び替えができるようになる。


## render {#render}

詳細は <https://datatables.net/reference/option/columns.render> 。

データを受け取ったあとに実行されて、表示テキストを変更することができる。

```js
render: function(data, type, row, meta) {
    return '<a href="/{{request.blueprint}}/' + data + '/edit">Edit</a>';
}
```

この例では主キーをハイパーリンクに変換している。

通貨表示にする場合は

```js
{ name: "salary", data: "salary", title: "Salary", render: ["number", ",", ".", 0, "&yen" ] },

```

1.  千の位ごとに","で区切る
2.  小数点は"."
3.  小数点以下"0"桁まで表示（=整数で表示）
4.  数値の前に&amp;yenをつける

(<https://datatables.net/manual/data/renderers#Number-helper>)
