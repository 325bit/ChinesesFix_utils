import os
from time import sleep


def read_ids_from_my_issue(file_path):
    """读取my_issue.txt中的ID并返回ID列表、ID对应行、表头、分隔线"""
    ids = []
    id_lines = {}
    header = ''
    separator = ''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if len(lines) >= 2:
                header = lines[0].strip()
                separator = lines[1].strip()
            for line in lines[2:]:
                parts = line.split('|')
                if len(parts) > 1:
                    id_value = parts[1].strip()
                    if id_value:
                        ids.append(id_value)
                        id_lines[id_value] = line.strip()
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在。")
    return ids, id_lines, header, separator

def search_ids_in_all_issue(all_issue_path, ids):
    """在all_issue.txt中搜索ID，并返回找到的ID列表"""
    found_ids = []
    try:
        with open(all_issue_path, 'r', encoding='utf-8') as file:
            all_lines = file.readlines()
            for id_value in ids:
                for line in all_lines:
                    if id_value in line:
                        found_ids.append(id_value)
                        break
    except FileNotFoundError:
        print(f"文件 {all_issue_path} 不存在。")
    return found_ids

def write_duplicates_to_file(output_path, duplicate_ids, id_lines, header, separator):
    """将重复内容写入duplicate_content.txt"""
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(f"{header}\n")
            file.write(f"{separator}\n")
            for id_value in duplicate_ids:
                line = id_lines.get(id_value)
                if line:
                    file.write(f"{line}\n")
    except IOError as e:
        print(f"写入文件 {output_path} 时发生错误: {e}")

def write_unique_issues_to_file(output_path, unique_ids, id_lines, header, separator):
    """将唯一内容写入unique_issues.txt"""
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(f"{header}\n")
            file.write(f"{separator}\n")
            for id_value in unique_ids:
                line = id_lines.get(id_value)
                if line:
                    file.write(f"{line}\n")
    except IOError as e:
        print(f"写入文件 {output_path} 时发生错误: {e}")

def main():
    my_issue_file = 'my_issue.txt'
    all_issue_file = 'all_issue.txt'
    output_duplicate = 'duplicate_content.txt'
    output_unique = 'unique_issues.txt'

    choice = input("请选择功能：【1】创建unique_issues.txt 【2】创建duplicate_content.txt\n请输入1或2：")

    ids, id_lines, header, separator = read_ids_from_my_issue(my_issue_file)
    if not ids:
        print("my_issue.txt中没有找到任何ID。")
        return

    duplicate_ids = search_ids_in_all_issue(all_issue_file, ids)

    if choice == '1':
        unique_ids = [id_val for id_val in ids if id_val not in duplicate_ids]
        write_unique_issues_to_file(output_unique, unique_ids, id_lines, header, separator)
        print(f"处理完成，唯一内容已写入 {output_unique}")
    elif choice == '2':
        write_duplicates_to_file(output_duplicate, duplicate_ids, id_lines, header, separator)
        print(f"处理完成，重复内容已写入 {output_duplicate}")
    else:
        print("输入错误，请输入1或2。")
    sleep(1)

if __name__ == '__main__':
    main()