#!/usr/bin/env python
# -*- coding:utf-8 -*-

# abs 求绝对值
print(abs(100))
print(abs(-100))

# 数据类型转换

print(int('1232323'))
print(int(122.3234))

print(float('12.3234'))
print(float('12'))

print(str(132.23))
print(str(112))

print(bool(1))
print(bool(0))
print(bool("djdj"))
print(bool(""))
print(bool(1.10))
print(bool(0.00))

# 定义函数 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:,然后，在缩进块中编写函数体，函数的返回值用return语句返回

def custom_function(number):
    if(number > 100):
        return number - 100
    else:
        return number + 100

print(custom_function(130))
print(custom_function(50))

# 空函数 pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
def nop():
    pass

age = 2
if age >= 18:
    pass

# 返回多个值

def custom_function1(number):
    return 100, 300

print(custom_function1(100))
print(custom_function1(100)[1])

# import math语句表示导入math包
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

# 位置参数
# x 的 n 次方
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(10, 5))

# 默认参数

# 必选参数在前，默认参数在后，否则Python的解释器会报错
def power1(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power1(10))
print(power1(10, 5))

def power2(name, age=12, language="中文"):
    print("%s 今年 %s 岁,擅长说 %s" % (name, age, language))

power2("小红")
power2("小明", language="英文")

# 可变参数
# 给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1, 2, 3]))

# 在参数前面加了一个*号,把函数的参数改为可变参数
def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc1(1, 2, 4))

# 关键字参数 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

# 命名关键字参数

def person1(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

def person2(name, age, *, city, job):
    print(name, age, city, job)

person2('Jack', 24, city='Beijing', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
# def person3(name, age, *args, city, job):
#     print(name, age, args, city, job)

# person3('Jack', 24, 'Beijing', 'Engineer')

# 参数组合

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

# 递归函数
# 计算阶乘n! = 1 x 2 x 3 x ... x n

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5))
print(fact(10))

# 递归调用的次数过多，会导致栈溢出
# fact(1000)

# 尾递归方式

def fact1(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact_iter(1, 10))
print(fact_iter(4, 100))