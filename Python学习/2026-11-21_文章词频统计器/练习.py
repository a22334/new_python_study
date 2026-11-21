# ==============================================
#  练习.py —— 自己动手，从零开始写！
#  主题：排序大作战（sorted / key=）
#  怎么用：
#   1. 先读题（注释就是题目）
#   2. 想清楚：输入是什么 → 怎么处理 → 输出什么
#   3. 删掉 pass 写代码
#   4. 取消底部对应行的注释，运行：python 练习.py
# ==============================================

# ---------------- 练习 1：数字排行榜 ----------------
# 写 practice1()：
#   1. 输入一串分数（空格隔开），例如：88 92 75 60 99 83
#   2. 转成整数列表
#   3. 用 sorted 输出：升序列表、降序列表
#   4. 再输出前三名（降序取前 3 个）
# 示例：
#   请输入分数：88 92 75 60 99 83
#   升序：[60, 75, 83, 88, 92, 99]
#   降序：[99, 92, 88, 83, 75, 60]
#   前三名：99 92 88
def practice1():
    while True:
        try:
            score = input('请输入一串分数(空格分开):')
            break
        except ValueError:
            print('请输入整数!')

        '''问题一:try-except结构形同虚设
                  这里不会出现ValueError
                  因为没有对输入的东西进行强制类型转换
        '''

    score_list = [int(x) for x in score.split()]
    print(f'升序列表:{sorted(score_list)}')
    print(f'降序列表:{sorted(score_list,reverse=True)}')
    reverse_score_list = sorted(score_list,reverse=True)
    print(f'前三名是{reverse_score_list[0:3]}')

    # AI修改建议

    # asc = sorted(score_list)
    # desc = sorted(score_list, reverse=True)
    # print(f'升序列表:{asc}')
    # print(f'降序列表:{desc}')
    # print(f'前三名是{" ".join(map(str, desc[:3]))}')

    '''
        map()函数
        map(函数,可迭代对象)

        nums = [1, 2, 3, 4]
        result = map(str, nums)      # 把每个元素转成字符串
        print(list(result))

        需要注意的是map返回的是一个迭代器 需要用list()进行转换

        迭代器
        只能使用一次 使用第二次就为空了
        所以 在刚刚那个例子中 再list(result) 就是空集了

    '''


# ---------------- 练习 2：姓名按长度排序 ----------------
# 写 practice2()：
#   1. 循环输入名字（每行一个，输入 end 结束），存进列表
#   2. 用 sorted(名单, key=len) 按名字长度从短到长排序
#   3. 输出排序结果，并标出每个名字的长度
# 示例：
#   请输入名字（end 结束）：li
#   请输入名字（end 结束）：zhangwei
#   请输入名字（end 结束）：wang
#   请输入名字（end 结束）：end
#   按长度排序：
#   li (2)
#   wang (4)
#   zhangwei (8)
def practice2():
    name_list = []
    while True:
        name = input("请输入名字('输入end结束'):")
        if name == 'end':
            break
        elif name in name_list:
            print('改名字已存在!')
        elif name == "":   # 问题 如果是" "那只会匹配一个空格 不能判断两个空格 但如果是"" 就可以直接判断是否为空
            print('名字无法为空!')
        else:
            name_list.append(name)
    name_list_sorted = sorted(name_list,key=len)
    for name in name_list_sorted:
        print(f'名字:{name},长度:{len(name)}')

# ---------------- 练习 3：词频统计器自己写（挑战题） ----------------
# 写 practice3()：完整版词频统计（不读文件，直接输入英文）
#   1. 循环输入英文句子（每行一句，输入 end 结束），拼成一个长文本
#   2. 自己写清洗：只保留字母（提示：join + isalpha），统一小写
#   3. 用字典计数，必须用 .get(w, 0) 的写法
#   4. 用 sorted(..., key=..., reverse=True) 输出出现最多的 5 个词
# 示例：
#   请输入（end 结束）：python is great python is fun
#   请输入（end 结束）：python is easy
#   请输入（end 结束）：end
#   出现最多的 5 个词：
#   python: 3 次
#   is: 3 次
#   great: 1 次
#   fun: 1 次
#   easy: 1 次
def practice3():
    sentence_list = []
    while True:
        sentence = input('请输入一个句子(输入end结束):')  #遇到的问题:要把每个输入的句子拼成长文 但是每次输入都会覆盖sentence 导致无法拼接
        if sentence == 'end':
            break
        sentence_list.append(sentence)

    words = " ".join(sentence_list)
    lower_words = words.lower()

    word_list = lower_words.split()

    clean_word_list = []

    for word in word_list:
        if not word.isalpha():
            continue
        clean_word_list.append(word)
    word_dict = {}

    for word in clean_word_list:
        word_dict[word] = word_dict.get(word,0) + 1

    finaly_word = sorted(word_dict.items(),key=lambda x:x[1],reverse=True)[:5] #遇到问题
     
    for number in range(len(finaly_word)):
        print(f'{finaly_word[number][0]}:{finaly_word[number][1]}次')

# ---------------- 运行入口 ----------------
# 一次只运行一个练习：把要运行那一行的 # 删掉即可
# practice1()
# practice2()
# practice3()
