# ================ 文章词频统计器（Python 学习进度恢复第 1 天） ================
# 说明：你的 Python 进度停在"密码生成器"，这个项目是它之后的第一个项目。
# 新知识点（重点）：
#   1. sorted() 排序 —— 带 key= 和 reverse= 参数
#   2. 字典方法 .get(键, 默认值) —— 取键值，没有就返回默认值（不报错）
# 复习：文件读写、split()、列表推导式、isalpha()、lower()、enumerate、字典计数
# 运行方法：在该文件夹打开终端，输入  python wordcount.py  回车
#         （文件夹里自带 article.txt 可以直接拿来统计）

import os

def read_text(filename):
    """读取文本文件，返回全部内容（复习：文件读写）"""
    if not os.path.exists(filename):
        return None
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def clean_word(word):
    """只保留字母，去掉标点符号（复习：列表推导式 + isalpha）"""
    return "".join(ch for ch in word if ch.isalpha())   # 只留字母，去掉 , . ! 等

def count_words(text):
    """统计每个单词出现次数 —— 新知识点：字典 .get(键, 默认值)"""
    counts = {}
    for word in text.split():                # 按空白切分
        w = clean_word(word).lower()         # 清干净 + 统一小写（大小写算同一个词）
        if w == "":                          # 跳过纯标点
            continue
        counts[w] = counts.get(w, 0) + 1     # 新知识点：get 取不到就默认 0，绝不报错
    return counts

def get_count(word):
    """给 sorted 当 key 用：返回这个词出现几次（新知识点：sorted 的 key=）"""
    return counts[word]

def main():
    filename = input("请输入文件名（例如 article.txt）：")
    text = read_text(filename)
    if text is None:
        print("❌ 找不到这个文件，请确认文件名（要带 .txt 后缀）")
        return

    counts = count_words(text)
    print(f"共统计到 {len(counts)} 个不同的单词")

    # 新知识点：sorted(可遍历, key=函数, reverse=True)
    #   key=   ：按"get_count(每个词) 的结果"排序（也就是按出现次数）
    #   reverse=True ：从大到小
    top = sorted(counts, key=get_count, reverse=True)[:10]   # 取前 10 个
    print("出现最多的 10 个单词：")
    for i, w in enumerate(top, 1):           # 复习：enumerate 编号
        print(f"{i}. {w} —— {counts[w]} 次")

main()
