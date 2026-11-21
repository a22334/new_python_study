# 最新的python学习内容

因为原来的那个仓库的文件夹出现了分裂 所以我让ai重新给我在这个文件夹中再慢慢生成每日学习内容 我再上传到这里

## 2026.11.21学习内容

1. sorted()排序
   常规的sorted排序的作用是按照列表内容的大小进行升序排列

   如果要进行逆序 也就是降序排列 sorted中有一个reverse值

   sorted(content,reverse = True)

   这样即可进行降序排列

   但其实 它的排列法则也是可以自定义的

   ```python
   def get_count(word):
   
    return counts[word]      # 返回这个词出现几次

    sorted(counts, key=get_count, reverse=True)

   意思：按 get_count(每个词) 的结果排序，也就是按"出现次数"从多到少
 
   ```

   也就是这里的key 我们可以通过定义一个函数对他进行操作

   当函数可以用lambda函数来表示时也可以用lambda进行

   除此之外还可以用len 也就是每个元素的长度来进行排序

   ```python
   number_list = ['hello','happy','good']
   
   sorted(number_list,key=len)
   
   ```

2. dict.get(key,默认值)

   从个人角度来说

   这个函数常用于 比如说计算一个列表中每个单词的出现次数 用字典的形式

   ```python
   number_list = ['hello','happy','good']
   
   word_emergency_dict = {}
   
   for word in number_list:

     word_emergency_dict[word] = word_emergency_dict.get(word,0) + 1
   ```
   我觉得还是挺好用的 以后也会多考虑用它

3. map()函数

   map(函数,可迭代对象)

   举个例子
   ```python
   nums = [1,2,3,4]

   result = map(str,nums)

   print(list(map))  #这里的输出会是['1','2','3','4'] 也就是把num的每个值从int变为了str

   map函数返回的数值是迭代器 所以只能取一次值 再取一次就变成空了
   ```

  
