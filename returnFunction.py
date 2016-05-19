#!/usr/bin/python
# -*- coding: UTF-8 -*-

#########################
#  闭包的理解  即一个函数内定义多个函数  并返回的是函数
#########################

def count():
    fs=[]
    for i in range(1,4):
        def f(j):
            def g():            # 循环变量会变化,故采用局部变量传值的方式来保证  结果的正确
                return j*j
            return g
        r=f(i)
        fs.append(r)
    return fs     #返回的是一个链表  链表里面是三个函数  f(1) f(2) f(3)
f2,f1,f3=count()   #count()其实是一个链表,所以可以一一赋值

print f1()
print f2()
print f3()

