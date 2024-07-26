import os
import json

# 定义输入文件夹和输出文件夹
input_folder = 'C:\\Users\\qizhi\\Desktop\\汉化\\窗社正式版\\script-cn-con2'
output_folder = 'C:\\Users\\qizhi\\Desktop\\汉化\\窗社正式版\\script-cn-con1'
original_folder = 'C:\\Users\\qizhi\\Desktop\\汉化\\窗社正式版\\script-jp-con1'  # 日文原版文件夹

# 如果输出文件夹不存在，则创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        original_path = os.path.join(original_folder, filename)

        # 读取汉化后的 JSON 文件
        with open(input_path, 'r', encoding='utf-8') as infile:
            translated_data = json.load(infile)

        # 读取日文原版 JSON 文件
        with open(original_path, 'r', encoding='utf-8') as origfile:
            original_data = json.load(origfile)

        # 转换数据格式
        decoded_data = []
        for trans_entry, orig_entry in zip(translated_data, original_data):
            for key, value in trans_entry.items():
                if ' & ' in key:
                    # 如果键中包含 ' & '，则将其拆分为 names 字段
                    names_list = key.split(' & ')
                    # 查找原版中的对应 names
                    orig_names = orig_entry.get("names", names_list)
                    decoded_data.append({"names": orig_names, "message": value})
                elif key == "旁白":
                    decoded_data.append({"message": value})
                else:
                    # 查找原版中的对应 name
                    orig_name = orig_entry.get("name", key)
                    decoded_data.append({"name": orig_name, "message": value})

        # 写入新的 JSON 文件
        with open(output_path, 'w', encoding='utf-8') as outfile:
            json.dump(decoded_data, outfile, ensure_ascii=False, indent=2)

print("解码完成！")