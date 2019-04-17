#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : input_text.py
# @Author: yu.jin
# @Date  : 2019-04-17
# @Desc  :

import tkinter as tk
# from tkinter import *
from tkinter import scrolledtext


top = tk.Tk()

L1 = tk.Label(top, text="输入url", width=20, height=5, padx=10, pady=10)
L1.pack(side=tk.LEFT)
E1 = tk.Entry(top, bd=5)
E1.pack(side=tk.RIGHT)

L2 = tk.Label(top, text="输入正则表达式", width=20, height=5, padx=10, pady=10)
L2.pack(side=tk.LEFT)
E2 = tk.Entry(top, bd=5)
E2.pack(side=tk.RIGHT)

def showinfo():
    # 获取输入的内容
    print(E1.get())
    print(E2.get())


button = tk.Button(top, text="按钮", command=showinfo, width=20, height=5, padx=20, pady=20)
button.pack()

top.mainloop()
