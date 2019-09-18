#!usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:chaowei
@file: globals_fun_test.py
@time: 2019/09/18
"""

from __future__ import print_function


abcde = 5
m = 4


def globals_test():
    str1 = "abcde.m"
    parts = str1.split(".")
    print("parts=", parts)

    return globals()[parts[0]]
    pass


if __name__ == '__main__':

    gt = globals_test()

    print("gt=", gt)

    pass