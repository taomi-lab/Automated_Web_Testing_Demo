# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : conftest.py
# @author   : TaoMi
# @Time     : 2024/7/30 下午3:06
from typing import List

import pytest

from common.driver import DriverOperate
from common.logger import GetLogger


def pytest_collection_modifyitems(config: "Config", items: List["Item"]):
    # items对象是pytest收集到的所有用例对象
    # 获取pytest.ini中的addopts值
    try:
        addopts = config.getini('addopts')
        if "--dist=each" in addopts:
            # 此时说明你要用的是多进程并发，我要得到当前的worker_id
            worker_id = config.workerinput.get('workerid')
        else:
            worker_id = None
    except:
        worker_id = None
    for item in items:
        # item就代表了一条用例
        if worker_id:
            item.originalname = item.originalname.encode('utf-8').decode("unicode-escape") + worker_id
            item._nodeid = item._nodeid.encode('utf-8').decode("unicode-escape") + worker_id
        else:
            item._nodeid = item._nodeid.encode('utf-8').decode("unicode-escape")


@pytest.fixture(scope='session', autouse=True)
def aalogger_init(worker_id):
    GetLogger.get_logger(worker_id).info('日志初始化成功')


@pytest.fixture(scope='session', autouse=True)
def init_driver():
    DriverOperate.globalDriverOperate = DriverOperate(browser='chrome')
    DriverOperate.globalDriverOperate.get('https://www.qunar.com/')
