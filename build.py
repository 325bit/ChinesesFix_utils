import os

# 打包 GitHub Scraper
os.system("pyinstaller --onefile --name GitHub_Issue_Scraper github_scraper.py")

# 打包 ID Searcher
os.system("pyinstaller --onefile --name ID_Searcher id_searcher.py")

print("打包完成！可执行文件在 dist 目录")