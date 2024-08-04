# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_login.py
# @author   : TaoMi
# @Time     : 2024/7/30 下午2:56
import allure
import pytest

from tools.read_json import read_json
from paths_manager import login_json
from common.driver import DriverOperate
from pages.page_login import PageLogin
from actions.loginactions import LoginActions

global_error_info = 0


def get_data_login(path):
    datas = read_json(path)
    print(datas)
    parameter = []
    for data in datas.values():
        parameter.append((data['username'], data['password'], data['success'], data['expect_result']))
    return parameter


# 测试登录
@allure.epic("去哪儿网站测试")
@allure.feature("登录测试")
class TestLogin:
    # username, password = "15135976034", "shs092121"
    parameter = get_data_login(login_json)

    @pytest.mark.parametrize("username, password, success, expect_result", parameter)
    def test_login(self, username, password, success, expect_result):
        allure.dynamic.title(f'{expect_result}')
        LoginActions().Longin(username, password)
        if success:
            flag = PageLogin().page_is_login_success()
            if flag:
                # 退出登录，为下一次登录做准备
                PageLogin().page_click_logout()
                PageLogin().page_click_login()
                PageLogin().page_click_pwd_login()
            else:
                DriverOperate.globalDriverOperate.screenshot()
                pytest.assume(flag)
        else:
            error_info = None
            if expect_result == "用户名或密码错误":
                error_info = PageLogin().page_get_error_info()
            elif expect_result == "登录失败":
                error_info = PageLogin().page_get_error_info1()
            # 刷新，为下一次输入做准备
            DriverOperate.globalDriverOperate.refresh()
            PageLogin().page_click_pwd_login()
            if expect_result != error_info:
                DriverOperate.globalDriverOperate.screenshot()
                pytest.assume(expect_result == error_info)
