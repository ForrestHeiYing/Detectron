#!usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:chaowei
@file: class_test.py
@time: 2019/09/18
"""
from __future__ import print_function


class A(object):
    def __init__(self, name):
        self.name = name
        self.name_2 = name + "_in_A"  # 父类的所有属性，子类都可用; 但都是优先调用父类的;方法也是如此
        print("name:", self.name)


class B(A):
    def __init__(self, name1):
        super(B, self).__init__(name1)
        print("hi....")
        self.name = name1 + " in B class"

    def getName(self):
        return "B: " + self.name_2

    pass


if __name__ == '__main__':

    b = B("hello")
    print(b.getName())

    pass