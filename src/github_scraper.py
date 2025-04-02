import os
import json
from github import Github, Auth
from github.GithubException import GithubException


def get_github_token():
    token_path = "github_token.txt"
    if os.path.exists(token_path):
        with open(token_path, "r") as f:
            token = f.read().strip()
            if validate_token(token):
                return token
    while True:
        token = input("请输入 GitHub Token: ").strip()
        if validate_token(token):
            with open(token_path, "w") as f:
                f.write(token)
            return token
        print("无效的 Token，请重新输入")


def validate_token(token):
    try:
        auth = Auth.Token(token)
        g = Github(auth=auth)
        g.get_user().login
        return True
    except GithubException:
        return False


def save_issues_to_file(repo, output_file):
    issues = repo.get_issues(state="all")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("")

    with open(output_file, "a", encoding="utf-8") as f:  # 改为追加模式
        for idx, issue in enumerate(issues, 1):
            issue_data = {
                "number": issue.number,
                "title": issue.title,
                "body": issue.body,
                "state": issue.state,
                "comments": [{"body": c.body} for c in issue.get_comments()],
                "url": issue.html_url
            }

            f.write(json.dumps(issue_data, ensure_ascii=False) + "\n\n----------------------------------------------------------------------------------\n\n")

            print(f"已保存 issue #{issue.number} 到 {output_file} ")

def main():
    token = get_github_token()
    g = Github(token)

    # 默认值为 acsigcn/ChinesesFix
    repo_name = input("请输入仓库名称 (格式: owner/repo), 默认: acsigcn/ChinesesFix: ").strip() or "acsigcn/ChinesesFix"
    
    try:
        repo = g.get_repo(repo_name)
    except GithubException:
        print("错误：仓库不存在或无权访问")
        return

    save_issues_to_file(repo, "all_issue.txt")
    print(f"已保存 {repo.issues_count} 个 issue 到 all_issue.txt")


if __name__ == "__main__":
    main()
