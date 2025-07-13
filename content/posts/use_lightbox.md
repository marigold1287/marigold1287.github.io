+++
title = "lightboxを使う"
author = ["K"]
date = 2024-02-19T22:08:00+09:00
lastmod = 2025-07-13T18:21:03+09:00
tags = ["hugo", "javascript"]
categories = ["tech"]
draft = false
showtoc = true
[build]
  publishResources = false
+++

## 公式HP {#公式hp}

<https://lokeshdhakar.com/projects/lightbox2/>


## インストール {#インストール}

<https://github.com/lokesh/lightbox2/releases> からzipファイルをダウンロードする。


## staticフォルダにファイルを移動する {#staticフォルダにファイルを移動する}

distフォルダの中身を `static/lightbox` フォルダに移動させる


## extend_head.html {#extend-head-dot-html}

`layouts/partials/extend_head.html` を作成し、

```html
<link href="{{ .Site.BaseURL }}lightbox/css/lightbox.css" rel="stylesheet" />
<script src="{{ .Site.BaseURL }}lightbox/js/lightbox-plus-jquery.min.js"></script>
```

を追記する。


## 使用例 {#使用例}

```org
#+attr_html: :rel lightbox[1] :height 200
[[file:/org/static/img/20230715/20230715_1.jpg][file:/org/static/img/20230715/thumbnail/20230715_1.jpg]]
```

こんな風に使う。

同じページにある画像を複数グループに分けたいときは
`:rel lightbox[1]` `:rel lightbox[2]` のように分ける。
