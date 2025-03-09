+++
title = "orgファイルをそのままhugoのcontentsフォルダに入れる"
author = ["K"]
date = 2025-02-27T08:00:59+09:00
lastmod = 2025-02-27T08:03:50+09:00
tags = ["hugo", "emacs"]
categories = ["tech"]
draft = false
showtoc = true
+++

## hugo new content {#hugo-new-content}

hugoで新しい記事を作る場合は `hugo new content post.md` でmarkdown形式のファイルを作ることができる。
orgの場合は `archetypes` に `default.org` というファイルを作って

```org
#+TITLE: {{ replace .File.ContentBaseName "-" " " | title }}
#+DATE: {{ .Date }}
#+AUTHOR: K
#+DRAFT: true
#+TAGS[]:
#+CATEGORIES:
```

としておくと、 `hugo new content post.org` で初期化されたファイルが出力される。ただ、これだとemacsを開くのが面倒なので `capture` を使って、hugoコマンドでファイルを生成した後に編集できるようにする。


## コード {#コード}

```lisp
(defun my/generate-hugo-article-file ()
  (let* ((title (read-string "Title: "))  ;; ユーザー入力を受け取る
         ;; (timestamp (format-time-string "%Y%m%d%H%M%S"))
         ;; (cmd (format "(cd ~/hugo/ks_room && hugo new content/post/%s-%s.org)" timestamp title))
         (hugo-dir "~/hugo/ks_room")
         (filename (concat title ".org"))
         (filepath (expand-file-name (concat "content/post/" filename) hugo-dir))
         (cmd (format "(cd %s && hugo new %s)" hugo-dir (shell-quote-argument filepath)))
         (output (shell-command-to-string cmd)))  ;; hugo new を実行
    (if (string-match-p "Content .* created" output)
        filepath  ;; 作成したファイルパスを返す
      (error "Failed to create Hugo post"))))  ;; エラーが発生した場合
```

-   User inputでtitleを入力する
-   hugo-dir: 適宜変更する
-   file-path: "content/post" の部分はThemeによるのでここも適宜変更する
-   cmd: hugoコマンドは `hugo.toml` があるフォルダでないと実行できないので移動してから実行する。
-   shell-quote-argument: スペース等の文字列がはいっていても機能するようにエスケープする。
-   shell-command-to-string: コマンドを実行
-   成功したらファイルパスを返す

`capture-template` は以下のようにする。

```elisp
(setq my-capture-templates
      '(("h" "Article for hugo" entry
         (file my/generate-hugo-article-file)
         "* %?"
         :unarrowed t
         :jump-to-captured t)))

(setq org-capture-templates my-capture-templates)
```

改善が必要なところ

-   タイムスタンプをファイル名につけてしまうとTITLEにも付いてしまうからコメントアウトしている
-   Capture時に `C-k` してもファイルは残ったまま


## 内部リンク {#内部リンク}

こんな感じでルートからの相対パスを書くか

<div class="verse">

</post/ホームページを開設してみる><br />

</div>

ショートコードを使って

<div class="verse">

\\<br />

</div>

書く


## 先頭にPROPERTIES DRAWERがあると上手くいかない {#先頭にproperties-drawerがあると上手くいかない}

org-roamとは相性が悪そう。

[gohugoio/hugo#9898 org-mode front matter ignored when document contains a pro...](https://github.com/gohugoio/hugo/issues/9898)


## ox-hugoを使ったほうが良い {#ox-hugoを使ったほうが良い}

[Using Org Mode With Hugo · weblog.masukomi.org](https://weblog.masukomi.org/2024/07/19/using-org-mode-with-hugo/)にきれいにまとめられているが、go-orgですべてを処理できるわけではないから、専用の変換ツールを使ったほうがいい。

PaperModというテーマを使っているのだが、 `custom-front-matter` を使えなくて苦労してしまった。
