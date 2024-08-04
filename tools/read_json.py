# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : read_json.py
# @author   : TaoMi
# @Time     : 2024/7/29 下午3:23

import os
import json


# 读取json文件的函数
def read_json(path):
    filepath = os.path.join(path)
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
