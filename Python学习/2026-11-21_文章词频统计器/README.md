# 今日项目（2026-11-21）：文章词频统计器（Python 进度恢复第 1 天）

你的 Python 进度停在**密码生成器**，这个项目是它之后的第一课。
打开一个文本文件，统计**每个单词出现多少次**，并排出出现最多的 10 个词——最简单的"文本分析"！
核心新知识：**sorted() 排序**（带 `key=`）和**字典的 .get() 方法**。

## 运行方法

在该文件夹打开终端：

```bash
python wordcount.py
```

输入文件名（文件夹里自带 `article.txt` 可以直接用）。

## 新知识点①：sorted() 排序（重点）

```python
sorted([3, 1, 2])                  # -> [1, 2, 3]（升序）
sorted([3, 1, 2], reverse=True)    # -> [3, 2, 1]（降序）
sorted("hello")                    # -> ['e', 'h', 'l', 'l', 'o']
```
注意：`sorted()` 返回**新列表**，不改变原来的。

**按特殊规则排序 —— key=**：
```python
def get_count(word):
    return counts[word]      # 返回这个词出现几次

sorted(counts, key=get_count, reverse=True)
# 意思：按 get_count(每个词) 的结果排序，也就是按"出现次数"从多到少
```
小例子：
```python
sorted(["aaa", "b", "cc"], key=len)   # 按长度排 -> ["b", "cc", "aaa"]
```

## 新知识点②：字典 .get(键, 默认值)

```python
counts = {"python": 3}

counts["java"]        # ❌ 报错！KeyError，键不存在
counts.get("java", 0) # -> 0（不报错，返回默认值）
```
所以"给一个词计数"最安全的写法：
```python
counts[w] = counts.get(w, 0) + 1   # 有就 +1，没有就从 0 开始 +1
```

## 复习：已经学过的

- 文件读写：`os.path.exists()` + `with open(..., "r", encoding="utf-8")`
- `text.split()` 切词、列表推导式 + `isalpha()` 清洗、`.lower()` 统一小写
- `enumerate(列表, 1)` 编号、字典计数、f-string

## 练习（真正的练习在 练习.py，从零写！）

**练习.py** 里 3 道题全是排序实战，从易到难：

1. **数字排行榜**（sorted 升/降序 + 取前 3 名）
2. **姓名按长度排序**（`sorted(名单, key=len)`）
3. **词频统计器自己写**（挑战：输入一段英文 → 清洗 → 字典计数 → top 5）

README 留两个热身小改：
1. 忽略长度 ≤ 2 的单词（提示：`if len(w) <= 2: continue`）
2. 额外输出"总单词数"（提示：`sum(counts.values())`）

## 小知识

词频统计是文本挖掘、搜索引擎、关键词提取的基础。`sorted()` 是**稳定排序**，Python 里排序又快又稳，写算法题、做排行榜都靠它。
