# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_buy_tickets2.py
# @author   : TaoMi
# @Time     : 2024/7/29 下午3:22
import allure
import pytest
from tools.read_json import read_json
from paths_manager import buytickes_json
from pages.page_buy_tickets import BuyLogin
from common.driver import DriverOperate
from actions.buy_ticketsactions import BuyticketsActions

global_var = 0


def get_data_login(buytickes_json):
    data = read_json(buytickes_json)
    arrs = []
    for data in data.values():
        arrs.append((data['start_station'], data['arrive_station'], data['time'], data['name'], data['boardcard'],
                     data['phone'], data['success'], data['except_result']))
    return arrs


# 测试登录
@allure.epic("去哪儿网站测试")
@allure.feature("买票测试")
class TestBuy:
    # ("北京","上海","2024-07-25","孙海森","142725199908224856","15135976034","True","None")
    parameter = get_data_login(buytickes_json)

    @pytest.mark.parametrize("start_station, arrive_station, date, name, boardcard, phone, success,expect_result",
                             parameter)
    def test_buy_tickets(self, start_station, arrive_station, date, name, boardcard, phone, success=None,
                         expect_result=None):
        allure.dynamic.title(f'{expect_result}')
        # 购票
        BuyticketsActions().Buytickets(start_station, arrive_station, date, name, boardcard, phone)
        # 如果购票成功，判断购票成功
        if success:
            try:
                # 标志购票成功
                flag = BuyLogin().page_submit_access
                # 四次回退到回退选择购票信息页面
                for _ in range(3):
                    DriverOperate.globalDriverOperate.driver.back()
                try:
                    # 判断是否在选票界面
                    assert BuyLogin().page_buy_is_logout_success()
                except:
                    DriverOperate.globalDriverOperate.screenshot()
                    pass
                # 已经为下一次测试用例做好准备
                pytest.assume(flag)
            except:
                DriverOperate.globalDriverOperate.screenshot()
        # 如果信息错误
        else:
            msg = BuyLogin().page_buy_get_error_info()
            try:
                assert msg == expect_result
                # 点击确认框
                BuyLogin().page_buy_click_button_ok()
                # 回退三次到火车票界面
                for _ in range(3):
                    DriverOperate.globalDriverOperate.driver.back()
                try:
                    # 判断是否在选票界面
                    pytest.assume(BuyLogin().page_buy_is_logout_success())
                except:
                    # 记录错误信息
                    DriverOperate.globalDriverOperate.screenshot()

            except AssertionError:
                DriverOperate.globalDriverOperate.screenshot()
