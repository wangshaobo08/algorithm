#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 20:50:47
# @Author  : sober (wangshaobo08@gmail.com)
# @Link    : https://www.jianshu.com/u/b2d5110e9a57
# @Version : $Id$


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left_li = merge_sort(arr[:mid])
    right_li = merge_sort(arr[mid:])
    left_cursor, right_cursor = 0, 0
    result = []
    while left_cursor < len(left_li) and right_cursor < len(right_li):
        if left_li[left_cursor] < right_li[right_cursor]:
            result.append(left_li[left_cursor])
            left_cursor += 1
        else:
            result.append(right_li[right_cursor])
            right_cursor += 1
    result += left_li[left_cursor:]
    result += right_li[right_cursor:]
    return result


if __name__ == "__main__":
    arr = [1, 2, 1, 4, 67, 3, 7, 8, 6, 5, 5]
    print(merge_sort(arr))
