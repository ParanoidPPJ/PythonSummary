#!/usr/bin/python
# -*- coding: UTF-8 -*-

###################################
## 被循环变量改变的闭包  返回也是函数
####################################

def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()

print f1()
print f2()
print f3()
