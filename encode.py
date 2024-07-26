import os
import json

# 定义输入文件夹和输出文件夹
input_folder = 'C:\\Users\\qizhi\\Desktop\\汉化\\窗社正式版\\script-jp-con1'
output_folder = 'C:\\Users\\qizhi\\Desktop\\汉化\\窗社正式版\\script-jp-con2'

# 如果输出文件夹不存在，则创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 读取 JSON 文件
        with open(input_path, 'r', encoding='utf-8') as infile:
            data = json.load(infile)

        # 转换数据格式
        converted_data = []
        for entry in data:
            if 'names' in entry:
                # 将 names 字段的值合并成一个字符串
                names_str = ' & '.join(entry['names'])
                converted_data.append({names_str: entry['message']})
            elif 'name' in entry:
                converted_data.append({entry['name']: entry['message']})
            else:
                converted_data.append({"旁白": entry['message']})

        # 写入新的 JSON 文件
        with open(output_path, 'w', encoding='utf-8') as outfile:
            json.dump(converted_data, outfile, ensure_ascii=False, indent=2)

print("转换完成！")