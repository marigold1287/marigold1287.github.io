+++
title = "datatables ordering設定"
author = ["K"]
date = 2025-03-17T07:54:27+09:00
lastmod = 2025-03-17T07:55:05+09:00
tags = ["javascript", "datatables"]
categories = ["tech"]
draft = false
showtoc = true
+++

## ordering {#ordering}

<https://datatables.net/reference/option/ordering>

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
    ordering: true,
})
```


## デフォルト条件の設定 {#デフォルト条件の設定}

<https://datatables.net/reference/option/order>

デフォルトはデータを読み込んだ順

```js
const table = $("#tableId").DataTable({
    ordering: true,
    order: []
})
```

2列目昇順、降順の場合は `"desc"` 。

```js
const table = $("#tableId").DataTable({
    ordering: true,
    order: [1, "asc"] // 0はじまり
})
```

複数列ソート、1列目・2列目の順で並べる。

```js
const table = $("#tableId").DataTable({
    ordering: true,
    order: [
        [0, 'asc'],
        [1, 'asc']
    ]
})
```

`columns` で `name` を指定している場合は

```js
const table = $("#tableId").DataTable({
    ordering: true,
    order: [
        {name: "registration_date", dir: "desc"},
        {name: "title", dir: "asc"},
        {name: "volume", dir: "asc"},
    ],

})
```

のように書くこともできる。


## クリック時の挙動を変更する {#クリック時の挙動を変更する}

<https://datatables.net/reference/option/columns.orderData>

ヘッダーをクリックしたときに複数列ソートをする場合は

```js
columns: [
    { orderData: [0, 1] },
    { orderData: 0 },
    { orderData: [2, 3, 4] },
]
```

`columns` の `orderData` プロパティに列番号をセットする。
`name` を使うことはできない?

昇順降順の切り替えは `orderSequence` で行う

```js
columns: [
    { orderData: [0, 1], orderSequence: ["asc", "desc"] },
    { orderData: 0, orderSequence: ["asc"] },
    { orderData: [2, 3, 4], orderSequence: ["asc", "desc", "desc"] },
]
```
