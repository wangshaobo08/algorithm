#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 15:49:55
# @Author  : sober (wangshaobo08@gmail.com)
# @Link    : https://www.jianshu.com/u/b2d5110e9a57
# @Version : $Id$

'''
	shell_sort base on insert_sort algorithm
'''


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while i > 0:
                if arr[i] < arr[i - gap]:
                    arr[i], arr[i - gap] = arr[i - gap], arr[i]
                    i -= gap
                else:
                    break
        gap //= 2
    print(arr)

if __name__ == "__main__":
    arr = [1, 2, 1, 4, 67, 3, 7, 8, 6, 5, 5]
    shell_sort(arr)
