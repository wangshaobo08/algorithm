#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-09 21:12:11
# @Author  : wangshaobo (370788717@qq.com)
# @Link    : https://www.jianshu.com/u/b2d5110e9a57
# @Version : $Id$

import os


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


if __name__ == "__main__":
    arr = [3, 4, 2, 1, 5, 7, 4, 7]
    bubble_sort(arr)
