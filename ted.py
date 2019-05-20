# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # 標題1
#
# ## 標題2
#
# ![Google](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)
#
# Latex： $\sqrt{a^2 + b ^ 2}$

import pandas as pd
df = pd.read_csv("ted_main.csv", encoding="utf-8")
df

# 單行操作：["行標籤名"] -> Series
df["comments"]

# 多行操作：[ ["標1"，"標2"，"標3"] ]
# 裡面[]：list 外面[]：行操作
df[ ["comments", "description"] ]

# 純粹耍帥一下：翻轉
df.T.to_csv("ted_transpose.csv", encoding="utf-8")
df.T
