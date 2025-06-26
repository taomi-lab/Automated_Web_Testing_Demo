# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : loginactions.py
# @author   : TaoMi
# @Time     : 2024/7/30 下午3:29

from common.driver import DriverOperate
from pages.page_login import PageLogin

global_first_flag = 1


class LoginActions:
    def Longin(self, username, password):
        # 点击去哪切换到登录界面-切换窗口-点击登录-点击账号密码登录-输入账号-输入密码-同意协议-点击登录-移动滑块-点击空白区域
        global global_first_flag
        page = PageLogin()
        if global_first_flag:
            page.page_click_please_login()
            page.page_change_window()
            page.page_click_login()
            page.page_click_pwd_login()
            global_first_flag = 0
        page.page_input_account(username)
        page.page_input_password(password)
        page.page_click_protocol()
        page.page_click_login_button()
        # 首先判断是否输入了账号 密码 以及点击协议

        # 点击了之后，就执行
        page.page_moving_verify_code()
        page.operate.base_move_to_empty_space()


if __name__ == '__main__':
    DriverOperate.globalDriverOperate = DriverOperate(browser='chrome')
    DriverOperate.globalDriverOperate.get('https://www.qunar.com/')
    LoginActions().Longin("15135976034", "shs092121")
    DriverOperate.globalDriverOperate.quit()
