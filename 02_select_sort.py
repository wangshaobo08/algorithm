#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-09 21:30:59
# @Author  : wangshaobo (370788717@qq.com)
# @Link    : https://www.jianshu.com/u/b2d5110e9a57
# @Version : $Id$


def selecet_sort(arr):
    n = len(arr)
    for j in range(n):
        for i in range(n - j):
            if arr[j] > arr[j + i]:
                arr[j], arr[j + i] = arr[j + i], arr[j]
    print(arr)

if __name__ == "__main__":
    arr = [1, 2, 1, 4, 67, 3, 7, 8, 6, 5, 5]
    selecet_sort(arr)
