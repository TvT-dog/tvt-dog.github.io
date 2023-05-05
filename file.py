import os
import random
# 定义函数，用于获取相对路径中的目录列表
def get_categories(rel_path):
    categories = []
    while True:
        rel_path, tail = os.path.split(rel_path)
        if tail:
            categories.insert(0, tail)
        else:
            if rel_path:
                categories.insert(0, rel_path)
            break
    return categories

# 定义函数，用于处理一个 md 文件
def process_md_file(filepath, out_dir):
    with open(filepath, "r", encoding="utf-8") as infile:
        content = infile.read()

    # 获取相对路径
    rel_path = os.path.relpath(filepath, os.getcwd())
    rel_dir, filename = os.path.split(rel_path)
    rel_dir = os.path.normpath(rel_dir)

    # 获取目录列表
    categories = get_categories(rel_dir)

    # 构建输出文件路径
    out_filepath = os.path.join(out_dir, filename)

    #创建随机数
    num=random.randint(1, 15)

    # 构建 YAML 头部
    yaml_header = "---\n"
    yaml_header += f"title: {filename[:-3]}\n"
    yaml_header += "categories:\n"
    yaml_header += f"- {categories}\n"
    yaml_header += f"index_img: /img/{num}.jpg\n"
    yaml_header += "---\n"

    # 写入到输出文件中
    with open(out_filepath, "w", encoding="utf-8") as outfile:
       # print(outfile)
        outfile.write(yaml_header)
        outfile.write(content)

# 定义函数，用于处理一个目录
def process_dir(dirname, out_dir):
    for root, dirs, files in os.walk(dirname):
        for file in files:
            if file.endswith(".md"):
                print(file)
                filepath = os.path.join(root, file)
                process_md_file(filepath, out_dir)
