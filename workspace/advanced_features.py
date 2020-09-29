#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 高级特性

# 切片
list1 = ["A", "B", "C", "D"]
print(list1)

# 切片方法取前N个元素
# [0:3]：从索引0开始取，直到索引3为止，但不包括索引3
print(list1[0:3])
# [1:3]：从索引1开始取，直到索引3为止，但不包括索引3
print(list1[1:3])

list2 = list(range(100))
print(list2)

# 取前十个数
print(list2[:10])

# 取后10个数
print(list2[-10:])

# 前11-20个数
print(list2[10:20])

# 前10个数，每两个取一个
print(list2[:10:2])

# 所有数，每5个取一个
print(list2[::5])

# 只写[:],原样复制一个list
print(list2[:])

# tuple也可以用切片操作，只是操作的结果仍是tuple
print((0, 1, 2, 3, 4, 5)[:3])


# 迭代
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for ch in 'ABC':
    print(ch)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

list10 = list(range(1, 11))
print(list10)

# 生成[1x1, 2x2, 3x3, ..., 10x10]
# 可以用循环，但循环比较繁琐
list11 = []
for x in range(1, 11):
    list11.append(x * x)
print(list11)

# 列表生成式则可以用一行语句代替循环生成上面的list：
print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([x * x * x for x in range(1, 11)])

print([m + n for m in 'ABC' for n in 'XYZ'])

import os
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }

# for循环同时使用两个甚至多个变量
for k, v in d.items():
    print(k, '=', v)

print([k + '=' + v for k, v in d.items()])

# 把一个list中所有的字符串变成小写
list20 = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in list20])

# if ... else
print([x for x in range(1, 11) if x % 2 == 0])

print([x if x % 2 == 0 else -x for x in range(1, 11)])

# 生成器
list30 = [x * x for x in range(10)]
print(list30)
g = (x * x for x in range(10))
print(g)
# 创建 list30 和g的区别仅在于最外层的[]和()，list30是一个list，而g是一个generator。
print(next(g))
print(next(g))
print(next(g))

g1 = (x * x for x in range(10))
for n in g1:
    print(n)

# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print('fib', b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print('fib',fib(10))

# 迭代器
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable。
from collections.abc import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance(1, Iterable))
print(isinstance(True, Iterable))
print(isinstance((x for x in range(10)), Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
from collections.abc import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))