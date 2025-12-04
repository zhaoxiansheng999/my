# -*- coding: utf-8 -*-
"""
Python 简易文本字数统计工具
支持：直接输入文本统计 + 读取 TXT 文件统计
无需额外依赖，Python 3.6+ 可直接运行
"""

def count_chars(text):
    """统计文本字符数：中文字数、英文字数、总字符数"""
    chinese_count = 0  # 中文字数
    english_count = 0  # 英文字数（大小写字母）
    total_count = len(text)  # 总字符数（含标点、空格、换行）
    
    for char in text:
        # 判断中文字符（Unicode 范围：0x4E00-0x9FFF）
        if '\u4e00' <= char <= '\u9fff':
            chinese_count += 1
        # 判断英文字符
        elif char.isalpha():
            english_count += 1
    
    return {
        "中文字数": chinese_count,
        "英文字数": english_count,
        "总字符数": total_count
    }

def main():
    print("=" * 40)
    print("🎉 Python 简易文本字数统计工具")
    print("=" * 40)
    print("请选择统计模式：")
    print("1. 直接输入文本统计")
    print("2. 读取本地 TXT 文件统计")
    print("=" * 40)
    
    while True:
        choice = input("请输入数字 1 或 2：")
        if choice in ["1", "2"]:
            break
        print("❌ 输入错误，请重新输入！")
    
    # 模式 1：直接输入文本
    if choice == "1":
        print("\n📝 请输入要统计的文本（输入完成后按回车，再输入 exit 结束）：")
        input_text = ""
        while True:
            line = input()
            if line == "exit":
                break
            input_text += line + "\n"
        if not input_text.strip():
            print("❌ 未输入任何文本！")
            return
        
    # 模式 2：读取 TXT 文件
    else:
        file_path = input("\n📂 请输入 TXT 文件路径（例如：C:/test.txt 或 ./test.txt）：")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                input_text = f.read()
        except FileNotFoundError:
            print(f"❌ 找不到文件：{file_path}")
            return
        except Exception as e:
            print(f"❌ 读取文件失败：{str(e)}")
            return
    
    # 统计并输出结果
    result = count_chars(input_text)
    print("\n" + "=" * 40)
    print("📊 统计结果")
    print("=" * 40)
    for key, value in result.items():
        print(f"{key}：{value}")
    print("=" * 40)

if __name__ == "__main__":
    main()
