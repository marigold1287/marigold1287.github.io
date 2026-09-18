import logging, re
import mkdocs.plugins

log = logging.getLogger("mkdocs")

# @mkdocs.plugins.event_priority(-50)
# def on_files(files, config):
#     # return
#     for file in files:
#         if file.is_documentation_page():
#             print(file.src_path)

# @mkdocs.plugins.event_priority(-50)
# def on_page_content(markdown, page, config, files):
#     # return
#     print(page.content)

@mkdocs.plugins.event_priority(-50)
def on_page_markdown(markdown, page, config, files):
        extra_meta_text = "\n\n## メタデータ\n"
        for key, value in page.meta.items():
            if key == "template" or key == "hide":
                continue
            if key.startswith("git") or "tags" in key:
                continue

            # 弾かれなかったメタデータをテキストとして追加
            extra_meta_text += f"- **{key}**: {value}\n"

        # もし追加すべきメタデータがあれば、markdownの末尾に結合する
        if extra_meta_text != "\n\n## メタデータ\n":
            markdown += extra_meta_text

        return markdown

