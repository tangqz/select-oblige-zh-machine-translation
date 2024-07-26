import os
import json

def count_lines_and_txruby(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        content = ''.join(lines)
        txruby_count = content.count('txruby')
    return len(lines), txruby_count

def compare_folders(folder1, folder2):
    folder1_files = {f for f in os.listdir(folder1) if f.endswith('.json')}
    folder2_files = {f for f in os.listdir(folder2) if f.endswith('.json')}
    
    common_files = folder1_files.intersection(folder2_files)
    
    for file_name in common_files:
        file1_path = os.path.join(folder1, file_name)
        file2_path = os.path.join(folder2, file_name)
        
        lines1, txruby_count1 = count_lines_and_txruby(file1_path)
        lines2, txruby_count2 = count_lines_and_txruby(file2_path)
        
        line_status = 'lineOK' if lines1 == lines2 else ('lineMismatch '+ str(lines1) + ' and ' + str(lines2))
        txruby_status = 'txrubyOK' if txruby_count1 == txruby_count2 else ('txrubyMismatch '+ str(txruby_count1) + ' and ' + str(txruby_count2))
        
        print(f"{file_name}: {line_status}, {txruby_status}")

# 示例文件夹路径
folder1 = 'C:\\Users\\qizhi\\Desktop\\汉化\\窗社正式版\\script-jp-con2'
folder2 = 'C:\\Users\\qizhi\\Desktop\\汉化\\窗社正式版\\script-cn-con2'

compare_folders(folder1, folder2)