#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : multi_thread_util.py
# @Author: yu.jin
# @Date  : 2019-04-26
# @Desc  :


def div_list(ls, n):
    """
    多线程切分列表，线上GPU机器共有 2个物理CPU，每个CPU 12个核
    :param ls:
    :param n:
    :return:
    """
    if not isinstance(ls, list) or not isinstance(n, int):
        return []
    ls_len = len(ls)
    if n <= 0 or 0 == ls_len:
        return []
    if n > ls_len:
        return []
    elif n == ls_len:
        return [[i] for i in ls]
    else:
        j = ls_len // n
        k = ls_len % n
        ### j,j,j,...(前面有n-1个j),j+k
        #步长j,次数n-1
        ls_return = []
        for i in range(0, (n-1) * j, j):
            ls_return.append(ls[i:i+j])
        #算上末尾的j+k
        ls_return.append(ls[(n-1) * j:])
        return ls_return
