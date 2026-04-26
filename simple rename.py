import os
import shutil

print("=== 批量文件复制并重命名程序启动 ===\n")

# 输入目录
input_dir = input("请输入【输入文件夹路径】：\n>>> ").strip()
output_dir = input("请输入【输出文件夹路径】：\n>>> ").strip()

print("\n=== 参数检查 ===")

# 检查输入目录
if not os.path.exists(input_dir):
    print("❌ 输入目录不存在！程序退出")
    exit()

if not os.path.isdir(input_dir):
    print("❌ 输入路径不是目录！程序退出")
    exit()

# 创建输出目录
if not os.path.exists(output_dir):
    print("输出目录不存在，正在创建...")
    os.makedirs(output_dir)
    print("输出目录创建完成")

print(f"\n输入目录: {input_dir}")
print(f"输出目录: {output_dir}")

print("\n=== 开始批量处理 ===")

file_count = 0
success_count = 0

for filename in os.listdir(input_dir):
    file_path = os.path.join(input_dir, filename)

    print(f"\n处理文件: {filename}")

    # 跳过目录
    if os.path.isdir(file_path):
        print("  -> 跳过（目录）")
        continue

    file_count += 1

    # 分割文件名
    parts = filename.split(".")
    if len(parts) < 2:
        print("  -> 跳过（格式不符合）")
        continue

    # 提取物种名
    species_raw = parts[0]
    print(f"  原始字段: {species_raw}")

    species_name = species_raw.replace("_", " ")
    print(f"  转换名称: {species_name}")

    # 判断类型
    if filename.endswith(".gff3"):
        new_filename = species_name + ".gff3"
        print("  类型: gff3")
    elif filename.endswith(".fa"):
        new_filename = species_name + ".fasta"
        print("  类型: fa → fasta")
    else:
        print("  -> 跳过（非目标类型）")
        continue

    new_path = os.path.join(output_dir, new_filename)
    print(f"  新文件: {new_filename}")

    # 避免覆盖
    if os.path.exists(new_path):
        print("  已存在，跳过")
        continue

    # 复制文件
    try:
        shutil.copy2(file_path, new_path)
        print("  成功")
        success_count += 1
    except Exception as e:
        print(f"  失败: {e}")

print("\n=== 处理完成 ===")
print(f"总文件数: {file_count}")
print(f"成功处理: {success_count}")
print(f"跳过/失败: {file_count - success_count}")
print("程序已完成，如果你有更好的建议欢迎致电：13100371621")