#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 15:26:20
# @Author  : sober (wangshaobo08@gmail.com)
# @Link    : https://www.jianshu.com/u/b2d5110e9a57
# @Version : $Id$


def quick_sort(arr, first, last):
    if first >= last:
        return
    mid_value = arr[first]
    low = first
    high = last
    while low < high:
        while low < high and arr[high] >= mid_value:
            high -= 1
        arr[low] = arr[high]
        # low += 1
        while low < high and arr[low] < mid_value:
            low += 1
        arr[high] = arr[low]
        # high -= 1
    arr[low] = mid_value
    quick_sort(arr, first, low - 1)
    quick_sort(arr, low + 1, last)


if __name__ == "__main__":
    arr = [1, 2, 1, 4, 67, 3, 7, 8, 6, 5, 5]
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print(arr)
