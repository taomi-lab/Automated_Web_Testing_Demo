# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : basepage.py
# @author   : TaoMi
# @Time     : 2024/7/29 下午4:35

from common.driver import DriverOperate


class BasePage:

    def __init__(self):
        self.operate: DriverOperate = DriverOperate.globalDriverOperate
