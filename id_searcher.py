import os

def read_ids_from_my_issue(file_path):
    """读取my_issue.txt中的ID并返回一个ID列表"""
    ids = []
    id_lines = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # 跳过前两行（表头和分隔线）
            lines = file.readlines()[2:]
            for line in lines:
                parts = line.split('|')
                if len(parts) > 1:
                    id_value = parts[1].strip()  # 提取ID
                    if id_value:
                        ids.append(id_value)
                        id_lines[id_value] = line.strip()  # 保存每个ID对应的行
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在。")
    return ids, id_lines

def search_ids_in_all_issue(all_issue_path, ids):
    """在all_issue.txt中搜索ID，并返回对应的ID及其所在行"""
    found_ids = []
    try:
        with open(all_issue_path, 'r', encoding='utf-8') as file:
            all_lines = file.readlines()
            for id_value in ids:
                for line in all_lines:
                    if id_value in line:  # 查找ID
                        found_ids.append(id_value)
                        break  # 找到一个ID后跳到下一ID，不重复搜索
    except FileNotFoundError:
        print(f"文件 {all_issue_path} 不存在。")
    return found_ids

def write_duplicates_to_file(output_path, duplicate_ids, id_lines):
    """将找到的重复内容写入duplicate_content.txt"""
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            # 写入表头
            file.write('''| 语句id                         | 英文文本                                  | 简体中文文本              | 建议修正文本              | 备注说明                       |
|--------------------------------|-------------------------------------------|---------------------------|---------------------------|-------------------------------|
''')
            # 写入重复的ID对应的行
            for id_value in duplicate_ids:
                line = id_lines.get(id_value)
                if line:
                    file.write(f"{line}\n")
    except IOError as e:
        print(f"写入文件 {output_path} 时发生错误: {e}")

def main():
    my_issue_file = 'my_issue.txt'
    all_issue_file = 'all_issue.txt'
    output_file = 'duplicate_content.txt'

    # 1. 从my_issue.txt读取ID及对应行
    ids, id_lines = read_ids_from_my_issue(my_issue_file)
    
    # 2. 在all_issue.txt中搜索这些ID
    duplicate_ids = search_ids_in_all_issue(all_issue_file, ids)
    
    # 3. 将找到的行写入duplicate_content.txt
    write_duplicates_to_file(output_file, duplicate_ids, id_lines)
    print(f"处理完成，找到的重复内容已写入 {output_file}")

if __name__ == '__main__':
    main()
