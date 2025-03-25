# ChinesesFix_utils

## 安装前置依赖

在终端中运行以下命令安装所需的依赖：

```bash
pip install pyinstaller
pip install pygithub
# 注意：新版本的 cryptography 可能会报错，推荐安装指定版本
pip install cryptography==41.0.2
```

## 生成可执行文件

然后运行 `build.py` 脚本来生成可执行文件：

```bash
python build.py
```

该脚本会生成两个可执行文件：

- `GitHub_Issue_Scraper.exe`
- `Issue_Filter.exe`

## GitHub Issue Scraper 使用说明

`GitHub_Issue_Scraper.exe` 会读取 `github_token.txt` 文件中的 GitHub Token。如果你的 Token 拥有对某个 repository 的访问权限，它将会抓取该 repository 中的 issues，并将其保存到 `all_issue.txt` 文件中。不知道什么是GitHub Token的问AI。

例如：

```bash
acsigcn/ChinesesFix
```

输入 `acsigcn/ChinesesFix`，`GitHub_Issue_Scraper.exe` 会抓取 `ChinesesFix` 仓库中的 issue 数据。

## Issue Filter 使用说明

`Issue_Filter.exe` 会读取 `my_issue.txt` 文件，并在 `all_issue.txt` 中查找每一行的 ID。如果 `all_issue.txt` 中包含该 ID，它将会将 `my_issue.txt` 中该 ID 所在的行输出到 `duplicate_content.txt` 文件中，或者删除 `my_issue.txt` 中对应的行，最后生成一个 `unique_issues.txt` 文件。

## 建议
建议大家在ChinesesFix提交issue的时候每个句子都附上id，方便唯一查找。


