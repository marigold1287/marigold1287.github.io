+++
title = "datatablesのpaging処理"
author = ["K"]
date = 2025-03-10T00:12:08+09:00
lastmod = 2025-03-10T00:41:30+09:00
tags = ["datatables", "javascript"]
categories = ["tech"]
draft = false
showtoc = true
+++

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
    paging: true,
    pageLength: 25,
    lengthMenu: [10, 25, 50, { label: 'All', value: -1 }]
})
```


## paging {#paging}

`false` の場合はすべてのデータがいっぺんに表示されるのでデータが多い場合は重くなってしまう。ただ、[serverSide]({{< relref "20250309113032-datatablesのserverside処理.md" >}})処理をしない限りは表示しようがしなかろうがすべてのデータを読み込むので重い場合はserverSideで処理すること。


## pageLength {#pagelength}

デフォルトは1ページあたり25データ。 `-1` にすると全件表示になる。


## lengthMenu {#lengthmenu}

DataTablesの上部に表示される件数選択部分の設定。
