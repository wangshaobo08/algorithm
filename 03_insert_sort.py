#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-09 22:06:24
# @Author  : wangshaobo (370788717@qq.com)
# @Link    : https://www.jianshu.com/u/b2d5110e9a57
# @Version : $Id$


def insert_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)


if __name__ == "__main__":
    arr = [12, 3, 5, 2, 5, 7, 5, 3]
    insert_sort(arr)
