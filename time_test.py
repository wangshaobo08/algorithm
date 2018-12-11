#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 17:08:07
# @Author  : sober (wangshaobo08@gmail.com)
# @Link    : https://www.jianshu.com/u/b2d5110e9a57
# @Version : $Id$

import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1

if __name__ == "__main__":
    countdown(100)

