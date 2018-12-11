#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-09 22:06:24
# @Author  : wangshaobo (370788717@qq.com)
# @Link    : https://www.jianshu.com/u/b2d5110e9a57
# @Version : $Id$
import timeit
import functools


def insert_sort1(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)


def insert_sort2(arr):
    n = len(arr)
    for j in range(n):
        i = j
        while i > 0:
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
            else:
                break
    print(arr)
if __name__ == "__main__":
    arr = [12, 3, 5, 2, 5, 7, 5, 3]
    insert_sort1(arr)
    print('---------')
    insert_sort2(arr)
    t1 = timeit.Timer(functools.partial(insert_sort1, arr))
    t2 = timeit.Timer(functools.partial(insert_sort2, arr))
    s1 = t1.timeit(10)
    s2 = t2.timeit(10)
    print("sort1:%s\nsort2:%s" % (s1, s2))
