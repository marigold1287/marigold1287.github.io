+++
title = "datatablesのserverSide処理"
author = ["K"]
date = 2025-03-09T14:59:34+09:00
lastmod = 2025-03-09T18:25:29+09:00
tags = ["datatables", "javascript", "flask", "python"]
categories = ["tech"]
draft = false
showtoc = true
+++

<https://datatables.net/reference/option/serverSide>


## 設定 {#設定}

初期化時に

```js
$("#tableId").DataTable({
    serverSide: true, // <- これを追加
    ajax: {
        url: "{{ url_for('.fetch_test') }}",
        type: "POST" // <- これを追加
    },
    columns: [
        { name: "name", data: "name", title: "Name",  },
        { name: "position", data: "position", title: "position",  },
        { name: "salary", data: "salary", title: "salary", },
        { name: "start_date", data: "start_date", title: "start_date",  },
        { name: "office", data: "office", title: "office",  },
        { name: "extn", data: "extn", title: "extn",  },
    ],
})
```

`serverSide: true` を加える。
serverSide処理ではサーバーにデータテーブルのインフォメーションが送信されるから `ajax` の設定に `type: "POST"` も加える。


## データ受け取り form形式 {#データ受け取り-form形式}

これをflaskで受け取る。

```python
from flask import request

params = request.form.to_dict()
```

中身は

```js
{'draw': '1', 'columns[0][data]': 'payslip_id', 'columns[0][name]': 'payslip_id_link', 'columns[0][searchable]': 'true', 'columns[0][orderable]': 'false', 'columns[0][search][value]': '', 'columns[0][search][regex]': 'false', 'columns[1][data]': 'payslip_id', 'columns[1][name]': 'payslip_id', 'columns[1][searchable]': 'true', 'columns[1][orderable]': 'true', 'columns[1][search][value]': '', 'columns[1][search][regex]': 'false', 'columns[2][data]': 'formatted_date', 'columns[2][name]': 'formatted_date', 'columns[2][searchable]': 'true', 'columns[2][orderable]': 'true', 'columns[2][search][value]': '', 'columns[2][search][regex]': 'false', 'columns[3][data]': 'salary', 'columns[3][name]': 'salary', 'columns[3][searchable]': 'true', 'columns[3][orderable]': 'true', 'columns[3][search][value]': '', 'columns[3][search][regex]': 'false', 'order[0][column]': '1', 'order[0][dir]': 'desc', 'order[0][name]': 'payslip_id', 'start': '0', 'length': '25', 'search[value]': '', 'search[regex]': 'false'}
```

<https://datatables.net/manual/server-side> に書いてあるとおりなのだが、こんなふうに受け取れる。
...これでは扱いにくい🤔🤔🤔

一応、

```python
def parse_parameters(params):
    parsed = params
    parsed['search'] = {
        "value": params.get('search[value]', ''),
        "regex": params.get('search[regex]', False)
    }
    parsed['draw'] = params.get('draw', 1)
    parsed['start'] = params.get('start', 0)
    parsed['length'] = params.get('length', -1)

    columns = []
    index = 0
    while f'columns[{index}][data]' in params:
        columns.append({
            'data': params[f'columns[{index}][data]'],
            'name': params[f'columns[{index}][name]'],
            'searchable': params[f'columns[{index}][searchable]'] == 'true',
            'orderable': params[f'columns[{index}][orderable]'] == 'true',
            'search': {
                'value': params[f'columns[{index}][search][value]'],
                'regex': params[f'columns[{index}][search][regex]'] == 'true',
            }
        })
        index += 1
    parsed['columns'] = columns

    orders = []
    index = 0
    while f'order[{index}][column]' in params:
        orders.append({
            'name': params[f'order[{index}][name]'],
            'dir': params[f'order[{index}][dir]'],
        })
        index += 1
    parsed['order'] = orders

    return parsed
```

というパーサは作っているからこれに噛ませればjson形式に変換できる。


## データ受け取り json形式 {#データ受け取り-json形式}

<https://stackoverflow.com/questions/24890420/how-to-process-server-side-parameter-sent-from-jquery-datatables-using-flask>
少し古い回答だが、これに少し手を加えればjson形式で受け取ることもできる。

まず `ajax` に

```js
ajax: {
    url: "{{ url_for('.fetch') }}",
    type: 'POST',
    contentType: 'application/json', // <-
    data: function ( args ) {  // <-
        return JSON.stringify( args );
    },
```

`contentType: 'application/json'` と `data: function ( args ) {return JSON.stringify( args );}` を加える。これでjson形式のパラメータをそのまま送ることができるようになる。

flask側で

```python
parsed = request.json
print(json.dumps(parsed, indent=4))
```

とすれば

```js
{
    "draw": 1,
    "columns": [
        {
            "data": "payslip_id",
            "name": "payslip_id_link",
            "searchable": true,
            "orderable": false,
            "search": {
                "value": "",
                "regex": false,
                "fixed": []
            }
        },
        {
        },
    ]
    ...
}
```

パースされた状態で受け取れる。
