import os
from pathlib import Path

# 获取项目根目录和src目录路径
ROOT_DIR = Path(__file__).parent
SRC_DIR = ROOT_DIR / "src"
DIST_DIR = ROOT_DIR / "dist"

def build_exe(script_name, exe_name):
    """通用打包函数"""
    cmd = f'pyinstaller --onefile --workpath "{ROOT_DIR / "build"}" --distpath "{DIST_DIR}" ' \
          f'--specpath "{ROOT_DIR}" --name "{exe_name}" "{SRC_DIR / script_name}"'
    print(f"正在打包 {script_name}...")
    os.system(cmd)

def main():
    # 确保dist目录存在
    DIST_DIR.mkdir(exist_ok=True)
    
    # 清理旧的打包文件
    for f in DIST_DIR.glob("*.exe"):
        f.unlink()
    
    # 打包两个脚本
    build_exe("github_scraper.py", "GitHub_Issue_Scraper")
    build_exe("issue_filter.py", "Issue_Filter")
    
    print(f"\n打包完成！可执行文件在 {DIST_DIR} 目录")

if __name__ == "__main__":
    main()