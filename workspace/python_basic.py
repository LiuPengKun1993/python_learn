#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 简单的输出
print('hello, world')

print('how', 'are', 'you')

print(1001 + 2010)

# 这里是注释

a = 10
# 当语句以冒号:结尾时，缩进的语句视为代码块
if a >= 0:
    print(a)
else:
    print(-a)

# 数据类型

# 整数 1，-1，0
print(1)

# 浮点数 0.1，3.14
print(3.14)

# 字符串
print('I\'m ok.')

# 布尔值
print(True)
print(3 > 2)

# and、or 和 not 运算符
print(True and True)
print(5 > 3 and 3 > 1)
print(True or True)
print(not True)

# 空值 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

# 变量
a = 1
a = 1 + a
print(a)

# 常量 所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量,
# 但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。

# Python的字符串
print(ord('A'))
print(ord('刘'))
print(chr(21016))
print('12'.encode('ascii'))
print(b'12'.decode('ascii'))

print('你%s' % '好')
print('这个是%s电脑, 需要%d元' % ('苹果', 10000))
# %s会把任何数据类型转换为字符串
print('这个是%s电脑, 需要%s元' % ('苹果', 10000))
# %%来表示一个%
print('今年销售额增长率是%d%%' % 12)

# format()
print('{0}, 今年销售额增长率是{1:.1f}%'.format('大家好', 12.0612332))

# f-string
w = 2.5
s = w ** 2
print(f'边长为 {w} 的正方形的面积是 is {s:.2f}')

# list
devect_list = ["huawei", "apple", "xiaomi"]
print(devect_list)
print(devect_list[0])
print(devect_list[-1])
print(len(devect_list))

devect_list.append("sanxing")
print(devect_list)

devect_list.insert(1, "rongyao")
print(devect_list)

devect_list.pop()
print(devect_list)

devect_list.pop(1)
print(devect_list)

devect_list[1] = "sanxing"
print(devect_list)

list1 = ["hello", 123, True]
print(list1)

# 二维数组
list2 = ["hello", list1, 1223, ["1", 12]]
print(list2)
print(list2[1][1])

list3 = []
print(list3)

# tuple tuple和list非常类似，但是tuple一旦初始化就不能修改，没有append()，insert()这样的方法
tuple1 = ('1', '2', '3')
print(tuple1)

tuple2 = ('1', '2', ["3", "4"])
print(tuple2)
tuple2[2][1] = "a"
print(tuple2)

# list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。

# 条件判断

age = 2
if age >= 18:
    print("已成年")
else:
    print("未成年")


if age >= 18:
    print("成年")
elif age >= 6:
    print("少年")
else:
    print("孩童")

# 循环
cities_list = ["北京", "上海", "深圳"]
for city in cities_list:
    print(city)

# 计算1+2+3+...+10000
# for x in ...
sum = 0
for i in list(range(10001)):
    sum = sum + i
print(sum)

# while循环

sum = 0
n = 10000
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)

# break
n = 1
while n <= 100:
    if n == 10:  # 当n = 10时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

# dict
dict1 = {"张三": 13, "李四": 18, "Bob": 15}
print(dict1)
print(dict1["张三"])

dict1["Tom"] = 20
print(dict1)

dict1["Tom"] = 200
print(dict1)

print('Bob' in dict1)
print('Bob1' in dict1)

dict1.pop("张三")
print(dict1)

# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。

# 而list相反：

# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。

dict2 = {"one": 1, "two": ["1", True], "three": dict1}
print(dict2)

dict2 = {"one": 1, "two": ["1", True], "two": dict1}
print(dict2)

# set set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

set1 = set([1, 2, 3])
print(set1)

set2 = set([1, 1, 2, 2, 3, 3])
print(set2)

set2.add(4)
set2.add(3)
print(set2)

set2.remove(4)
print(set2)