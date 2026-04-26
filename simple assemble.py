import glob
import os

# 让用户输入输入目录
while True:
    input_dir = input("请输入包含待合并文件的文件夹路径：").strip('"')

    if not os.path.isdir(input_dir):
        print("路径不存在，请重新输入！\n")
    else:
        break

# 让用户输入文件匹配规则
while True:
    pattern_input = input(
        "\n请输入要查找的文件类型或匹配规则：\n"
        "（支持中文文件名，例如：*测试*.txt）\n"
        "支持以下输入格式（输入内容 → 实际匹配效果）：\n"
        "  fa          → *.fa\n"
        "  .fa         → *.fa\n"
        "  *.fa        → *.fa\n"
        "  fa.gz       → *.fa.gz\n"
        "  *测试*.txt  → 匹配包含“测试”的 txt 文件\n"
        "  data_??.csv → data_??.csv（? 表示单个字符）\n"
        "请输入："
    ).strip()

    if not pattern_input:
        print("输入不能为空，请重新输入！\n")
        continue

    if not any(char in pattern_input for char in ["*", "?", "."]):
        pattern = f"*.{pattern_input}"
    elif pattern_input.startswith("."):
        pattern = f"*{pattern_input}"
    else:
        pattern = pattern_input

    break

files = glob.glob(os.path.join(input_dir, pattern))

if not files:
    print(f"该目录下没有找到匹配 {pattern} 的文件，请检查输入！")
    exit()

print(f"\n✅ 找到 {len(files)} 个匹配文件（规则：{pattern}）\n")

# === 输出文件名（支持中文）===
while True:
    output_name = input(
        "\n请输入输出文件名（必须包含完整文件名和后缀，支持中文，例如：合并结果.fa）："
    ).strip()

    if not output_name:
        print("文件名不能为空，请重新输入！\n")
        continue

    if "." not in output_name or output_name.endswith("."):
        print("文件名必须包含后缀（例如：merged.fa），请重新输入！\n")
        continue

    invalid_chars = r'<>:"/\|?*'
    if any(c in output_name for c in invalid_chars):
        print("文件名包含非法字符（<>:\"/\\|?*），请重新输入！\n")
        continue

    break

# === 输出路径（自动创建）===
while True:
    output_dir = input(
        "\n请输入输出文件保存位置（文件夹路径）：\n"
        "规则说明：\n"
        "  - 支持中文路径，例如：E:\\数据\\结果\n"
        "  - 如果路径不存在，将自动创建该文件夹\n"
        "  - 不要输入文件名，只输入文件夹路径\n"
        "请输入："
    ).strip('"')

    if not output_dir:
        print("路径不能为空，请重新输入！\n")
        continue

    # 如果不存在则创建
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"路径不存在，已自动创建：{output_dir}")
        except Exception as e:
            print(f"创建文件夹失败：{e}\n")
            continue

    break

output_file = os.path.join(output_dir, output_name)

total_size = 0

with open(output_file, "w", encoding="utf-8") as outfile:
    for i, fname in enumerate(files, 1):
        size = os.path.getsize(fname) / (1024 * 1024)
        print(f"[{i}/{len(files)}] 正在处理: {fname} ({size:.2f} MB)")
        
        with open(fname, encoding="utf-8", errors="ignore") as infile:
            for line in infile:
                outfile.write(line)

        total_size += size
        print(f"已累计写入约 {total_size:.2f} MB\n")

print(f"搞定了！恭喜你看到这一行，如果你有更好的建议欢迎致电：13100371621.输出文件：{output_file}")